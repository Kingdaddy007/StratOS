#!/usr/bin/env python3
"""Build, validate, and safely install Anti-Gravity OS.

The development CLI intentionally uses only Python's standard library. Release
payloads are built in CI, so end users do not need Python to consume them.
"""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
import re
import shutil
import stat
import sys
import tempfile
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
GLOBAL_ROOT = REPO_ROOT / "global"
MANIFEST_PATH = GLOBAL_ROOT / "manifest.yaml"
SUPPORTED_HOSTS = ("antigravity", "gemini", "codex", "cursor", "windsurf", "opencode")
INSTALL_OPTIONS = ("general", "full")
ANTIGRAVITY_RULE_MAX_CHARACTERS = 12_000
MUTATION_CLASSES = (
    "read_only",
    "local_edit",
    "dependency_or_network",
    "destructive",
    "external_or_production",
)
WORKFLOW_REQUIRED_FIELDS = (
    "id",
    "version",
    "status",
    "intent",
    "use_when",
    "do_not_use_when",
    "inputs",
    "required_resources",
    "mutation_class",
    "approval_gates",
    "states",
    "outputs",
    "verification",
    "failure_paths",
    "resume_contract",
    "next_workflows",
    "profiles",
)
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FUNCTIONAL_OWNERS = {
    "studio_support",
    "product_strategy",
    "systems_architecture",
    "design_direction",
    "staff_engineering",
    "assurance_quality",
}
AGENT_REQUIRED_FIELDS = (
    "id",
    "name",
    "description",
    "functional_owner",
    "delivery_role",
    "profiles",
    "activation",
    "exclusions",
    "default_mutation_class",
    "allowed_mutation_classes",
    "tool_capabilities",
    "primary_agent",
    "subagent",
    "can_delegate",
    "model_tier",
    "command_policy",
    "skills",
    "return_contract",
    "delegation_contract",
)
AGENT_OPTIONAL_FIELDS = ("conditional_skills",)
AGENT_ALLOWED_FIELDS = set(AGENT_REQUIRED_FIELDS) | set(AGENT_OPTIONAL_FIELDS)
AGENT_RETURN_CONTRACT_REQUIREMENTS = (
    ("scope",),
    ("input", "provenance"),
    ("authority",),
    ("evidence",),
    ("finding", "decision"),
    ("confidence",),
    ("conflict",),
    ("recommendation",),
    ("stop", "escalate"),
    ("residual",),
    ("owner",),
)
CANONICAL_AGENT_TOOL_CAPABILITIES = {
    "read_file",
    "list_files",
    "search_text",
    "edit_file",
    "run_command",
}
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
UNRESOLVED_TOKEN_PATTERN = re.compile(
    r"(?<!\$)\{\{[A-Za-z_][A-Za-z0-9_.-]*\}\}"
)
PERSONAL_PATH_PATTERNS = (
    re.compile(r"(?i)file:///+[a-z]:/users/"),
    re.compile(r"(?i)[a-z]:[\\/]users[\\/]"),
    re.compile(r"(?i)file:///+[a-z]%3a/users/"),
    re.compile(r"(?i)/users/(?:godsw|oviks)(?:/|$)"),
)


class AntiGravityError(RuntimeError):
    """Base error for predictable CLI failures."""


class InstallationRefused(AntiGravityError):
    """Raised when an installation target or approval state is unsafe."""


class ValidationFailed(AntiGravityError):
    """Raised when a build is attempted with invalid canonical source."""


def utc_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json_atomic(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    try:
        temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


@contextmanager
def exclusive_file_lock(path: Path, timeout_seconds: float = 5.0):
    deadline = time.monotonic() + timeout_seconds
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor: int | None = None
    while descriptor is None:
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(descriptor, str(os.getpid()).encode("ascii"))
        except FileExistsError:
            try:
                stale = time.time() - path.stat().st_mtime > 30
            except FileNotFoundError:
                stale = False
            if stale:
                path.unlink(missing_ok=True)
                continue
            if time.monotonic() >= deadline:
                raise TimeoutError(f"Timed out acquiring workflow index lock: {path}")
            time.sleep(0.05)
    try:
        yield
    finally:
        os.close(descriptor)
        path.unlink(missing_ok=True)


def write_workflow_state(workspace: Path, state: dict[str, Any]) -> Path:
    required = {
        "schema_version",
        "task_id",
        "workflow_id",
        "mode",
        "status",
        "current_state",
        "completed_states",
        "owner",
        "workspace",
        "evidence",
        "artifacts",
        "approvals",
        "blockers",
        "next_action",
        "created_at",
        "updated_at",
        "archived",
    }
    missing = required - set(state)
    if missing:
        raise ValueError(f"Workflow state is missing: {', '.join(sorted(missing))}")
    task_id = state["task_id"]
    if not isinstance(task_id, str) or not re.fullmatch(r"[A-Za-z0-9._-]+", task_id):
        raise ValueError("task_id must contain only letters, digits, dot, underscore, or hyphen")
    if state["schema_version"] != 1:
        raise ValueError("Unsupported workflow state schema_version")

    state_directory = workspace.resolve() / ".agents" / "workflows"
    state_path = state_directory / f"{task_id}.json"
    write_json_atomic(state_path, state)

    index_path = state_directory / "index.json"
    lock_path = state_directory / ".index.lock"
    with exclusive_file_lock(lock_path):
        if index_path.exists():
            index = load_json(index_path)
        else:
            index = {"schema_version": 1, "updated_at": state["updated_at"], "tasks": {}}
        tasks = index.setdefault("tasks", {})
        tasks[task_id] = state_path.name
        index["updated_at"] = state["updated_at"]
        write_json_atomic(index_path, index)
    return state_path


def file_map(root: Path) -> dict[str, Path]:
    if not root.exists():
        return {}
    return {
        path.relative_to(root).as_posix(): path
        for path in root.rglob("*")
        if path.is_file()
    }


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return ""
    if value in {"null", "~"}:
        return None
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if re.fullmatch(r"-?[0-9]+", value):
        return int(value)
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(item) for item in inner.split(",")]
    if value.startswith(("\"", "'")) and value.endswith(value[0]):
        if value[0] == "\"":
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                pass
        return value[1:-1]
    return value


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the deliberately small YAML subset used by OS metadata.

    Supported constructs are top-level scalar keys, inline lists, block lists,
    one-level mappings inside a block list, and folded/literal scalar blocks.
    Deeper nested mappings belong in JSON registry files rather than Markdown
    frontmatter.
    """

    result: dict[str, Any] = {}
    lines = text.replace("\r\n", "\n").split("\n")
    index = 0
    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            index += 1
            continue
        if raw.startswith((" ", "\t")) or ":" not in raw:
            raise ValueError(f"Unsupported YAML at line {index + 1}: {raw}")
        key, raw_value = raw.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if not re.fullmatch(r"[A-Za-z0-9_-]+", key):
            raise ValueError(f"Invalid key at line {index + 1}: {key}")

        if raw_value in {">", "|"}:
            block: list[str] = []
            index += 1
            while index < len(lines):
                candidate = lines[index]
                if candidate and not candidate.startswith((" ", "\t")):
                    break
                block.append(candidate.strip())
                index += 1
            separator = " " if raw_value == ">" else "\n"
            result[key] = separator.join(part for part in block if part).strip()
            continue

        if raw_value == "":
            items: list[Any] = []
            index += 1
            while index < len(lines):
                candidate = lines[index]
                if candidate and not candidate.startswith((" ", "\t")):
                    break
                item = candidate.strip()
                if item:
                    if not item.startswith("-"):
                        raise ValueError(
                            f"Only block lists are supported at line {index + 1}"
                        )
                    value = item[1:].strip()
                    if ":" not in value:
                        items.append(parse_scalar(value))
                        index += 1
                        continue

                    item_key, item_value = value.split(":", 1)
                    item_key = item_key.strip()
                    if not re.fullmatch(r"[A-Za-z0-9_-]+", item_key):
                        raise ValueError(f"Invalid nested key at line {index + 1}: {item_key}")
                    mapping: dict[str, Any] = {item_key: parse_scalar(item_value.strip())}
                    index += 1
                    while index < len(lines):
                        continuation = lines[index]
                        if continuation and not continuation.startswith((" ", "\t")):
                            break
                        nested = continuation.strip()
                        if not nested:
                            index += 1
                            continue
                        if nested.startswith("-"):
                            break
                        if ":" not in nested:
                            raise ValueError(
                                f"Only one-level mappings are supported at line {index + 1}"
                            )
                        nested_key, nested_value = nested.split(":", 1)
                        nested_key = nested_key.strip()
                        if not re.fullmatch(r"[A-Za-z0-9_-]+", nested_key):
                            raise ValueError(
                                f"Invalid nested key at line {index + 1}: {nested_key}"
                            )
                        if nested_key in mapping:
                            raise ValueError(
                                f"Duplicate nested key at line {index + 1}: {nested_key}"
                            )
                        mapping[nested_key] = parse_scalar(nested_value.strip())
                        index += 1
                    items.append(mapping)
                    continue
                index += 1
            result[key] = items
            continue

        result[key] = parse_scalar(raw_value)
        index += 1
    return result


def split_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    content = path.read_text(encoding="utf-8-sig")
    normalized = content.replace("\r\n", "\n")
    if not normalized.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = normalized.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unclosed YAML frontmatter")
    metadata = parse_simple_yaml(normalized[4:end])
    return metadata, normalized[end + 5 :]


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationFailed(f"Unable to load {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationFailed(f"Expected an object in {path}")
    return value


def load_manifest(repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    path = repo_root / "global" / "manifest.yaml"
    return load_json(path)


def issue(code: str, path: Path | str, message: str) -> dict[str, str]:
    return {"code": code, "path": str(path), "message": message}


def validate_skill_files(repo_root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    for path in sorted((repo_root / "global" / "skills").rglob("SKILL.md")):
        relative = path.relative_to(repo_root)
        try:
            metadata, _ = split_frontmatter(path)
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            problems.append(issue("skill-frontmatter", relative, str(exc)))
            continue
        unexpected = set(metadata) - {"name", "description", "license"}
        if unexpected:
            problems.append(
                issue(
                    "skill-frontmatter-keys",
                    relative,
                    f"unsupported canonical keys: {', '.join(sorted(unexpected))}",
                )
            )
        name = metadata.get("name")
        description = metadata.get("description")
        if not isinstance(name, str) or not SKILL_NAME_PATTERN.fullmatch(name):
            problems.append(issue("skill-name", relative, "name must be hyphen-case"))
        elif name != path.parent.name:
            problems.append(
                issue("skill-name-folder", relative, f"name must match folder {path.parent.name}")
            )
        if not isinstance(description, str) or not description.strip():
            problems.append(issue("skill-description", relative, "description is required"))
        elif len(description) > 1024:
            problems.append(
                issue("skill-description-length", relative, "description exceeds 1024 characters")
            )
        ui_metadata_path = path.parent / "agents" / "openai.yaml"
        if not ui_metadata_path.exists():
            problems.append(issue("skill-ui-metadata", relative, "agents/openai.yaml is missing"))
        else:
            ui_metadata = ui_metadata_path.read_text(encoding="utf-8-sig", errors="replace")
            for field in ("interface:", "display_name:", "short_description:", "default_prompt:"):
                if field not in ui_metadata:
                    problems.append(
                        issue(
                            "skill-ui-metadata",
                            ui_metadata_path.relative_to(repo_root),
                            f"missing {field.rstrip(':')}",
                        )
                    )
    return problems


def validate_agent_files(repo_root: Path) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]]]:
    """Validate portable agent contracts before an adapter renders host files."""
    problems: list[dict[str, str]] = []
    agents: dict[str, dict[str, Any]] = {}
    directory = repo_root / "global" / "agents"
    for path in sorted(directory.glob("*/AGENT.md")):
        relative = path.relative_to(repo_root)
        try:
            metadata, _ = split_frontmatter(path)
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            problems.append(issue("agent-frontmatter", relative, str(exc)))
            continue
        missing = [field for field in AGENT_REQUIRED_FIELDS if field not in metadata]
        if missing:
            problems.append(issue("agent-fields", relative, f"missing fields: {', '.join(missing)}"))
            continue
        unexpected = set(metadata) - AGENT_ALLOWED_FIELDS
        if unexpected:
            problems.append(
                issue(
                    "agent-frontmatter-keys",
                    relative,
                    f"unsupported canonical keys: {', '.join(sorted(unexpected))}",
                )
            )
        agent_id = metadata["id"]
        if not isinstance(agent_id, str) or not SKILL_NAME_PATTERN.fullmatch(agent_id):
            problems.append(issue("agent-id", relative, "id must be hyphen-case"))
            continue
        if agent_id != path.parent.name or metadata.get("name") != agent_id:
            problems.append(issue("agent-name", relative, "id and name must match the agent folder"))
        if agent_id in agents:
            problems.append(issue("agent-duplicate", relative, f"duplicate id {agent_id}"))
        agents[agent_id] = metadata
        if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
            problems.append(issue("agent-description", relative, "description is required"))
        if metadata.get("functional_owner") not in FUNCTIONAL_OWNERS:
            problems.append(issue("agent-owner", relative, "unknown functional_owner"))
        if metadata.get("delivery_role") not in {
            "orchestrator",
            "functional_lead",
            "independent_assurance",
        }:
            problems.append(issue("agent-role", relative, "invalid delivery_role"))
        for field in (
            "profiles",
            "activation",
            "exclusions",
            "allowed_mutation_classes",
            "tool_capabilities",
            "skills",
            "return_contract",
            "delegation_contract",
        ):
            if not isinstance(metadata.get(field), list) or not metadata[field]:
                problems.append(issue("agent-field-type", relative, f"{field} must be a non-empty list"))
            elif any(not isinstance(value, str) or not value.strip() for value in metadata[field]):
                problems.append(issue("agent-field-type", relative, f"{field} entries must be non-empty strings"))
        if isinstance(metadata.get("return_contract"), list):
            return_text = " ".join(metadata["return_contract"]).lower()
            missing_return_requirements = [
                "/".join(terms)
                for terms in AGENT_RETURN_CONTRACT_REQUIREMENTS
                if not any(term in return_text for term in terms)
            ]
            if missing_return_requirements:
                problems.append(
                    issue(
                        "agent-return-contract",
                        relative,
                        "return_contract must cover: " + ", ".join(missing_return_requirements),
                    )
                )
        if metadata.get("default_mutation_class") not in MUTATION_CLASSES:
            problems.append(issue("agent-mutation", relative, "invalid default_mutation_class"))
        allowed = metadata.get("allowed_mutation_classes", [])
        if any(value not in MUTATION_CLASSES for value in allowed):
            problems.append(issue("agent-mutation", relative, "invalid allowed_mutation_classes"))
        elif metadata.get("default_mutation_class") not in allowed:
            problems.append(issue("agent-mutation", relative, "default mutation must be allowed"))
        if any(value not in CANONICAL_AGENT_TOOL_CAPABILITIES for value in metadata.get("tool_capabilities", [])):
            problems.append(issue("agent-tools", relative, "unknown canonical tool capability"))
        if metadata.get("model_tier") not in {"inherit", "flash", "pro"}:
            problems.append(issue("agent-model", relative, "invalid model_tier"))
        if metadata.get("command_policy") not in {"off", "sandbox"}:
            problems.append(issue("agent-command-policy", relative, "invalid command_policy"))
        for field in ("primary_agent", "subagent", "can_delegate"):
            if not isinstance(metadata.get(field), bool):
                problems.append(issue("agent-field-type", relative, f"{field} must be boolean"))
        conditional_skills = metadata.get("conditional_skills", [])
        if not isinstance(conditional_skills, list):
            problems.append(issue("agent-conditional-skills", relative, "conditional_skills must be a list"))
        else:
            for index, selection in enumerate(conditional_skills):
                if not isinstance(selection, dict) or set(selection) != {"profiles", "skills"}:
                    problems.append(
                        issue(
                            "agent-conditional-skills",
                            relative,
                            f"conditional_skills[{index}] must contain only profiles and skills",
                        )
                    )
                    continue
                for field in ("profiles", "skills"):
                    values = selection[field]
                    if not isinstance(values, list) or not values or any(
                        not isinstance(value, str) or not SKILL_NAME_PATTERN.fullmatch(value)
                        for value in values
                    ):
                        problems.append(
                            issue(
                                "agent-conditional-skills",
                                relative,
                                f"conditional_skills[{index}].{field} must be a non-empty hyphen-case list",
                            )
                        )
    return problems, agents


def validate_workflow_files(repo_root: Path) -> tuple[list[dict[str, str]], dict[str, dict[str, Any]]]:
    problems: list[dict[str, str]] = []
    workflows: dict[str, dict[str, Any]] = {}
    directory = repo_root / "global" / "workflows"
    for path in sorted(directory.glob("workflow-*.md")):
        relative = path.relative_to(repo_root)
        try:
            metadata, _ = split_frontmatter(path)
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            problems.append(issue("workflow-frontmatter", relative, str(exc)))
            continue
        missing = [field for field in WORKFLOW_REQUIRED_FIELDS if field not in metadata]
        if missing:
            problems.append(
                issue("workflow-fields", relative, f"missing fields: {', '.join(missing)}")
            )
        workflow_id = metadata.get("id")
        if not isinstance(workflow_id, str) or not SKILL_NAME_PATTERN.fullmatch(workflow_id):
            problems.append(issue("workflow-id", relative, "id must be hyphen-case"))
            continue
        if workflow_id in workflows:
            problems.append(issue("workflow-duplicate", relative, f"duplicate id {workflow_id}"))
        workflows[workflow_id] = metadata
        if metadata.get("mutation_class") not in MUTATION_CLASSES:
            problems.append(issue("workflow-mutation", relative, "invalid mutation_class"))
        for field in (
            "use_when",
            "do_not_use_when",
            "inputs",
            "required_resources",
            "approval_gates",
            "states",
            "outputs",
            "verification",
            "failure_paths",
            "next_workflows",
            "profiles",
        ):
            if field in metadata and not isinstance(metadata[field], list):
                problems.append(issue("workflow-field-type", relative, f"{field} must be a list"))

    known = set(workflows)
    for workflow_id, metadata in workflows.items():
        for next_id in metadata.get("next_workflows", []):
            if next_id in {None, "none", "None", ""}:
                continue
            if next_id not in known:
                problems.append(
                    issue(
                        "workflow-route",
                        directory / f"workflow-{workflow_id}.md",
                        f"unknown next workflow: {next_id}",
                    )
                )
    return problems, workflows


def validate_context_templates(repo_root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    directory = repo_root / "global" / "context_templates"
    for path in sorted(directory.glob("*.md")):
        if path.name in {"AGENTS.md", "README.md"}:
            continue
        relative = path.relative_to(repo_root)
        try:
            metadata, _ = split_frontmatter(path)
        except (OSError, UnicodeDecodeError, ValueError) as exc:
            problems.append(issue("context-frontmatter", relative, str(exc)))
            continue
        if metadata.get("status") != "template":
            problems.append(issue("context-status", relative, "status must be template"))
        for field in ("scope", "project_id", "updated_at", "owner", "confidence"):
            if field not in metadata:
                problems.append(issue("context-metadata", relative, f"missing {field}"))
    return problems


def validate_adapters(repo_root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    required = {
        "schema_version",
        "host",
        "namespace",
        "content_root",
        "instruction_target",
        "skills_target",
        "workflows_target",
        "supports_slash_commands",
        "approval_model",
        "capabilities",
    }
    for host in SUPPORTED_HOSTS:
        path = repo_root / "global" / "adapters" / host / "adapter.json"
        if not path.exists():
            problems.append(issue("adapter-missing", path.relative_to(repo_root), "adapter is missing"))
            continue
        try:
            adapter = load_json(path)
        except ValidationFailed as exc:
            problems.append(issue("adapter-json", path.relative_to(repo_root), str(exc)))
            continue
        missing = required - set(adapter)
        if missing:
            problems.append(issue("adapter-fields", path.relative_to(repo_root), f"missing {sorted(missing)}"))
        if adapter.get("host") != host or adapter.get("namespace") != "antigravity":
            problems.append(issue("adapter-identity", path.relative_to(repo_root), "host or namespace mismatch"))
        if host == "antigravity":
            agent_fields = {"agents_target", "agent_format", "agent_tool_map"}
            missing_agent_fields = agent_fields - set(adapter)
            if missing_agent_fields:
                problems.append(
                    issue(
                        "adapter-agents",
                        path.relative_to(repo_root),
                        f"missing {sorted(missing_agent_fields)}",
                    )
                )
            elif adapter.get("agent_format") != "antigravity-markdown":
                problems.append(
                    issue("adapter-agents", path.relative_to(repo_root), "unsupported agent_format")
                )
            else:
                mapped = adapter.get("agent_tool_map", {})
                missing_tools = CANONICAL_AGENT_TOOL_CAPABILITIES - set(mapped)
                if missing_tools or any(not isinstance(value, str) or not value for value in mapped.values()):
                    problems.append(
                        issue(
                            "adapter-agents",
                            path.relative_to(repo_root),
                            "agent_tool_map must cover every canonical capability",
                        )
                    )
            global_install = adapter.get("global_install")
            required_global_fields = {
                "root_name",
                "instruction_target",
                "router_target",
                "user_profile_target",
                "skills_target",
                "workflows_target",
                "agents_target",
                "payload_target",
            }
            if host == "antigravity":
                if not isinstance(global_install, dict):
                    problems.append(
                        issue(
                            "adapter-global-install",
                            path.relative_to(repo_root),
                            "antigravity adapter must declare global_install targets",
                        )
                    )
                else:
                    missing_global_fields = required_global_fields - set(global_install)
                    if missing_global_fields:
                        problems.append(
                            issue(
                                "adapter-global-install",
                                path.relative_to(repo_root),
                                f"missing {sorted(missing_global_fields)}",
                            )
                        )
        capabilities = adapter.get("capabilities", {})
        for capability in (
            "read_file",
            "list_files",
            "search_text",
            "edit_file",
            "run_command",
            "request_approval",
        ):
            if not capabilities.get(capability):
                problems.append(
                    issue("adapter-capability", path.relative_to(repo_root), f"missing {capability}")
                )
    return problems


def distributable_markdown(repo_root: Path) -> Iterable[Path]:
    global_root = repo_root / "global"
    roots = (
        global_root / "skills",
        global_root / "workflows",
        global_root / "core",
        global_root / "baselines",
        global_root / "context_templates",
        global_root / "global_templates",
        global_root / "reference",
        global_root / "design-audit",
        global_root / "agents",
    )
    for root in roots:
        if root.exists():
            yield from root.rglob("*.md")
    for path in (global_root / "GEMINI.md", global_root / "GLOBAL_MEMORY.md"):
        if path.exists():
            yield path


def validate_markdown(repo_root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    for path in sorted(set(distributable_markdown(repo_root))):
        relative = path.relative_to(repo_root)
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if path == repo_root / "global" / "GEMINI.md" and len(text) > ANTIGRAVITY_RULE_MAX_CHARACTERS:
            problems.append(
                issue(
                    "gemini-policy-length",
                    relative,
                    f"exceeds Antigravity's {ANTIGRAVITY_RULE_MAX_CHARACTERS}-character rule limit",
                )
            )
        if path.parent.name == "workflows" and UNRESOLVED_TOKEN_PATTERN.search(text):
            problems.append(issue("unresolved-token", relative, "contains unresolved {{...}} token"))
        for pattern in PERSONAL_PATH_PATTERNS:
            if pattern.search(text.replace("\\", "/")):
                problems.append(issue("personal-path", relative, "contains a personal absolute path"))
                break
        for raw_link in MARKDOWN_LINK_PATTERN.findall(text):
            link = raw_link.strip().split("#", 1)[0]
            if not link or link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if link.lower().startswith("file:///"):
                problems.append(issue("absolute-link", relative, f"non-portable link: {raw_link}"))
                continue
            if re.match(r"(?i)^[a-z]:[\\/]", link):
                problems.append(issue("absolute-link", relative, f"non-portable link: {raw_link}"))
                continue
            candidate = (path.parent / link.replace("%20", " ")).resolve()
            if candidate.suffix.lower() == ".md" and not candidate.exists():
                problems.append(issue("broken-link", relative, f"missing target: {raw_link}"))
    return problems


def validate_forbidden_files(repo_root: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    forbidden_directories = (
        repo_root / "global" / "projects",
        repo_root / "global" / "global_workflows",
    )
    for path in forbidden_directories:
        if path.exists():
            problems.append(issue("forbidden-directory", path.relative_to(repo_root), "must not exist"))
    for path in (repo_root / "global").rglob("*.bak"):
        problems.append(issue("backup-file", path.relative_to(repo_root), "tracked backup file is forbidden"))
    return problems


def validate_manifest(
    repo_root: Path,
    workflows: dict[str, dict[str, Any]],
    agents: dict[str, dict[str, Any]],
) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    path = repo_root / "global" / "manifest.yaml"
    if not path.exists():
        return [issue("manifest-missing", path.relative_to(repo_root), "manifest is missing")]
    try:
        manifest = load_manifest(repo_root)
    except ValidationFailed as exc:
        return [issue("manifest-json", path.relative_to(repo_root), str(exc))]
    if manifest.get("schema_version") != 2:
        problems.append(issue("manifest-version", path.relative_to(repo_root), "schema_version must be 2"))
    if set(manifest.get("hosts", [])) != set(SUPPORTED_HOSTS):
        problems.append(issue("manifest-hosts", path.relative_to(repo_root), "host registry mismatch"))
    if set(manifest.get("mutation_classes", [])) != set(MUTATION_CLASSES):
        problems.append(issue("manifest-mutations", path.relative_to(repo_root), "mutation registry mismatch"))

    profiles = manifest.get("profiles", [])
    definitions = manifest.get("profile_definitions", {})
    if set(definitions) != set(profiles):
        problems.append(issue("manifest-profiles", path.relative_to(repo_root), "profile definitions mismatch"))
    elif definitions.get("general") != {"kind": "base", "extends": []}:
        problems.append(
            issue("manifest-profiles", path.relative_to(repo_root), "general must be the sole base profile")
        )
    else:
        for profile_id, definition in definitions.items():
            if profile_id == "general":
                continue
            if definition.get("kind") != "pack" or definition.get("extends") != ["general"]:
                problems.append(
                    issue(
                        "manifest-profiles",
                        path.relative_to(repo_root),
                        f"{profile_id} must be a pack extending general",
                    )
                )
            profile_path = repo_root / "global" / "profiles" / profile_id / "profile.json"
            if not profile_path.exists():
                problems.append(
                    issue("manifest-profile-path", path.relative_to(repo_root), f"missing profile file for {profile_id}")
                )

    registries = (
        "skills",
        "workflows",
        "context_templates",
        "baselines",
        "templates",
        "resources",
        "agents",
    )
    for registry_name in registries:
        seen: set[str] = set()
        for entry in manifest.get(registry_name, []):
            entry_id = entry.get("id")
            entry_path = entry.get("path")
            if entry_id in seen:
                problems.append(issue("manifest-duplicate", path.relative_to(repo_root), f"duplicate {entry_id}"))
            seen.add(entry_id)
            if not isinstance(entry_path, str) or not (repo_root / entry_path).exists():
                problems.append(
                    issue("manifest-path", path.relative_to(repo_root), f"missing path for {entry_id}: {entry_path}")
                    )
            destination = entry.get("destination")
            if destination is not None and (
                not isinstance(destination, str)
                or not destination
                or Path(destination).is_absolute()
                or ".." in Path(destination).parts
            ):
                problems.append(
                    issue("manifest-destination", path.relative_to(repo_root), f"invalid destination for {entry_id}")
                )
            if entry.get("functional_owner") not in FUNCTIONAL_OWNERS:
                problems.append(
                    issue("manifest-owner", path.relative_to(repo_root), f"invalid owner for {entry_id}")
                )
            if not isinstance(entry.get("delivery_role"), str) or not entry["delivery_role"]:
                problems.append(
                    issue("manifest-role", path.relative_to(repo_root), f"missing delivery role for {entry_id}")
                )
            for profile in entry.get("profiles", []):
                if profile not in profiles:
                    problems.append(
                        issue("manifest-profile", path.relative_to(repo_root), f"unknown profile {profile}")
                    )
            if registry_name == "agents":
                compatibility = entry.get("host_compatibility", [])
                if not isinstance(compatibility, list) or not compatibility:
                    problems.append(
                        issue("manifest-agent-host", path.relative_to(repo_root), f"missing host compatibility for {entry_id}")
                    )
                elif any(host not in manifest.get("hosts", []) for host in compatibility):
                    problems.append(
                        issue("manifest-agent-host", path.relative_to(repo_root), f"unknown agent host for {entry_id}")
                    )

    manifest_workflows = {entry.get("id") for entry in manifest.get("workflows", [])}
    if manifest_workflows != set(workflows):
        missing = sorted(set(workflows) - manifest_workflows)
        stale = sorted(manifest_workflows - set(workflows))
        problems.append(
            issue(
                "manifest-workflows",
                path.relative_to(repo_root),
                f"registry mismatch; missing={missing}, stale={stale}",
            )
        )

    disk_skills = {
        skill.parent.name for skill in (repo_root / "global" / "skills").rglob("SKILL.md")
    }
    manifest_skills = {entry.get("id") for entry in manifest.get("skills", [])}
    if disk_skills != manifest_skills:
        problems.append(
            issue(
                "manifest-skills",
                path.relative_to(repo_root),
                f"registry mismatch; missing={sorted(disk_skills - manifest_skills)}, stale={sorted(manifest_skills - disk_skills)}",
            )
        )
    for agent_id, metadata in agents.items():
        declared_skills = set(metadata.get("skills", []))
        for selection in metadata.get("conditional_skills", []):
            if isinstance(selection, dict):
                declared_skills.update(selection.get("skills", []))
                for profile in selection.get("profiles", []):
                    if profile not in profiles:
                        problems.append(
                            issue(
                                "agent-conditional-profile",
                                path.relative_to(repo_root),
                                f"{agent_id} selects unknown profile {profile}",
                            )
                        )
        missing_skills = sorted(declared_skills - disk_skills)
        if missing_skills:
            problems.append(
                issue(
                    "agent-skills",
                    path.relative_to(repo_root),
                    f"{agent_id} references missing skills: {', '.join(missing_skills)}",
                )
            )
    manifest_agents = {entry.get("id") for entry in manifest.get("agents", [])}
    if manifest_agents != set(agents):
        problems.append(
            issue(
                "manifest-agents",
                path.relative_to(repo_root),
                f"registry mismatch; missing={sorted(set(agents) - manifest_agents)}, stale={sorted(manifest_agents - set(agents))}",
            )
        )
    return problems


def validate_routing_fixtures(
    repo_root: Path, workflows: dict[str, dict[str, Any]]
) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    path = repo_root / "tests" / "fixtures" / "routing.json"
    if not path.exists():
        return [issue("routing-fixtures", path.relative_to(repo_root), "fixture file is missing")]
    try:
        fixture = load_json(path)
        manifest = load_manifest(repo_root)
    except ValidationFailed as exc:
        return [issue("routing-fixtures", path.relative_to(repo_root), str(exc))]
    if fixture.get("schema_version") != 3:
        problems.append(issue("routing-version", path.relative_to(repo_root), "schema_version must be 3"))
    required = {
        "id",
        "request",
        "route_kind",
        "route",
        "base_profile",
        "active_packs",
        "functional_leads",
        "mode",
        "maximum_mutation_class",
        "approval_required",
    }
    seen: set[str] = set()
    valid_modes = {"diagnose", "propose", "implement", "incident-mitigate"}
    routes_by_kind = {
        "workflow": workflows,
        "skill": {entry.get("id"): entry for entry in manifest.get("skills", [])},
    }
    for scenario in fixture.get("scenarios", []):
        missing = required - set(scenario)
        scenario_id = scenario.get("id", "<unknown>")
        if missing:
            problems.append(
                issue("routing-fields", path.relative_to(repo_root), f"{scenario_id} missing {sorted(missing)}")
            )
            continue
        if scenario_id in seen:
            problems.append(
                issue("routing-duplicate", path.relative_to(repo_root), f"duplicate scenario {scenario_id}")
            )
        seen.add(scenario_id)
        route_kind = scenario["route_kind"]
        route = scenario["route"]
        if route_kind not in routes_by_kind:
            problems.append(
                issue(
                    "routing-route-kind",
                    path.relative_to(repo_root),
                    f"{scenario_id} has invalid route_kind {route_kind!r}",
                )
            )
        elif route not in routes_by_kind[route_kind]:
            problems.append(
                issue(
                    "routing-route",
                    path.relative_to(repo_root),
                    f"{scenario_id} references unknown {route_kind} {route}",
                )
            )
        if scenario["base_profile"] != "general":
            problems.append(
                issue("routing-profile", path.relative_to(repo_root), f"{scenario_id} must use the general base")
            )
        active_packs = scenario["active_packs"]
        if not isinstance(active_packs, list) or len(active_packs) != len(set(active_packs)):
            problems.append(
                issue("routing-packs", path.relative_to(repo_root), f"{scenario_id} active_packs must be unique")
            )
        elif any(
            pack not in manifest.get("profiles", [])
            or manifest["profile_definitions"].get(pack, {}).get("kind") != "pack"
            for pack in active_packs
        ):
            problems.append(
                issue("routing-packs", path.relative_to(repo_root), f"{scenario_id} has an invalid pack")
            )
        elif route_kind in routes_by_kind and route in routes_by_kind[route_kind]:
            route_profiles = set(routes_by_kind[route_kind][route].get("profiles", []))
            selected_profiles = {"general", *active_packs}
            if not route_profiles & selected_profiles:
                problems.append(
                    issue(
                        "routing-route-profile",
                        path.relative_to(repo_root),
                        f"{scenario_id} routes {route_kind} {route} outside selected profiles",
                    )
                )
        functional_leads = scenario["functional_leads"]
        known_leads = {entry["functional_owner"] for entry in manifest.get("agents", [])}
        if not isinstance(functional_leads, list) or not functional_leads:
            problems.append(
                issue("routing-leads", path.relative_to(repo_root), f"{scenario_id} must select a lead")
            )
        elif any(lead not in known_leads for lead in functional_leads):
            problems.append(
                issue("routing-leads", path.relative_to(repo_root), f"{scenario_id} has an unknown lead")
            )
        if scenario["mode"] not in valid_modes:
            problems.append(
                issue("routing-mode", path.relative_to(repo_root), f"{scenario_id} has invalid mode")
            )
        mutation = scenario["maximum_mutation_class"]
        if mutation not in MUTATION_CLASSES:
            problems.append(
                issue("routing-mutation", path.relative_to(repo_root), f"{scenario_id} has invalid mutation")
            )
        if scenario["mode"] == "diagnose" and mutation != "read_only":
            problems.append(
                issue("routing-diagnose", path.relative_to(repo_root), f"{scenario_id} diagnosis must be read-only")
            )
        if mutation in {"destructive", "external_or_production"} and not scenario["approval_required"]:
            problems.append(
                issue("routing-approval", path.relative_to(repo_root), f"{scenario_id} requires approval")
            )
    if not fixture.get("scenarios"):
        problems.append(issue("routing-empty", path.relative_to(repo_root), "no routing scenarios declared"))
    return problems


def validate_repository(repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    problems: list[dict[str, str]] = []
    problems.extend(validate_forbidden_files(repo_root))
    problems.extend(validate_skill_files(repo_root))
    agent_problems, agents = validate_agent_files(repo_root)
    problems.extend(agent_problems)
    workflow_problems, workflows = validate_workflow_files(repo_root)
    problems.extend(workflow_problems)
    problems.extend(validate_context_templates(repo_root))
    problems.extend(validate_adapters(repo_root))
    problems.extend(validate_markdown(repo_root))
    problems.extend(validate_manifest(repo_root, workflows, agents))
    problems.extend(validate_routing_fixtures(repo_root, workflows))
    return {"ok": not problems, "issue_count": len(problems), "issues": problems}


def filesystem_path(path: Path) -> str:
    """Return a Windows-safe filesystem path without changing portable metadata."""
    resolved = str(path.resolve())
    if os.name != "nt" or resolved.startswith("\\\\?\\"):
        return resolved
    if resolved.startswith("\\\\"):
        return "\\\\?\\UNC\\" + resolved[2:]
    return "\\\\?\\" + resolved


def copy_entry(
    source: Path, destination: Path, additional_ignores: tuple[str, ...] = ()
) -> None:
    if source.is_dir():
        ignored_names = (
            "*.bak",
            "__pycache__",
            "README.md",
            "CHANGELOG.md",
            *additional_ignores,
        )
        shutil.copytree(
            filesystem_path(source),
            filesystem_path(destination),
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns(*ignored_names),
        )
    else:
        os.makedirs(filesystem_path(destination.parent), exist_ok=True)
        shutil.copy2(filesystem_path(source), filesystem_path(destination))


def validate_payload(payload: Path) -> list[dict[str, str]]:
    problems: list[dict[str, str]] = []
    text_extensions = {".md", ".json", ".yaml", ".yml", ".txt", ".toml"}
    for path in payload.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(payload)
        if path.suffix.lower() == ".bak" or "projects" in relative.parts:
            problems.append(issue("payload-forbidden", relative, "forbidden runtime artifact"))
        if path.suffix.lower() not in text_extensions:
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if UNRESOLVED_TOKEN_PATTERN.search(text):
            problems.append(issue("payload-token", relative, "unresolved template token"))
        normalized = text.replace("\\", "/")
        if any(pattern.search(normalized) for pattern in PERSONAL_PATH_PATTERNS):
            problems.append(issue("payload-path", relative, "personal absolute path"))
        if path.suffix.lower() != ".md":
            continue
        for raw_link in MARKDOWN_LINK_PATTERN.findall(text):
            link = raw_link.strip().split("#", 1)[0]
            if not link or link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if link.lower().startswith("file:///") or re.match(r"(?i)^[a-z]:[\\/]", link):
                problems.append(issue("payload-link", relative, f"non-portable link: {raw_link}"))
                continue
            candidate = (path.parent / link.replace("%20", " ")).resolve()
            if candidate.suffix.lower() == ".md" and not os.path.exists(filesystem_path(candidate)):
                problems.append(issue("payload-link", relative, f"missing target: {raw_link}"))
    return problems


def resolve_pack_selection(
    manifest: dict[str, Any], profile: str | None, packs: Iterable[str] = ()
) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Resolve legacy --profile and explicit pack requests into stable composition."""
    requested: list[str] = []
    if profile and profile != "general":
        requested.append(profile)
    for raw_pack in packs:
        for pack in raw_pack.split(","):
            value = pack.strip()
            if value:
                requested.append(value)

    definitions = manifest.get("profile_definitions", {})
    for pack in requested:
        if pack == "general":
            raise AntiGravityError("general is implicit; use --profile general or omit --packs")
        definition = definitions.get(pack)
        if definition is None or definition.get("kind") != "pack":
            raise AntiGravityError(f"Unknown optional pack: {pack}")

    requested_set = set(requested)
    ordered_packs = tuple(
        profile_id
        for profile_id in manifest["profiles"]
        if profile_id != "general" and profile_id in requested_set
    )
    return ("general", *ordered_packs), ordered_packs


def install_option_counts(repo_root: Path = REPO_ROOT) -> dict[str, int]:
    """Return live manifest counts used by the interactive install question."""
    manifest = load_manifest(repo_root)
    skills = manifest.get("skills", [])
    return {
        "agents": len(manifest.get("agents", [])),
        "workflows": len(manifest.get("workflows", [])),
        "general_skills": sum("general" in entry.get("profiles", []) for entry in skills),
        "all_skills": len(skills),
    }


def resolve_install_option(
    repo_root: Path,
    option: str | None,
    profile: str,
    packs: Iterable[str],
    interactive: bool | None = None,
) -> tuple[str, list[str], str]:
    """Resolve General or Full selection before a payload is built or installed."""
    supplied_packs = list(packs)
    if option is not None and option not in INSTALL_OPTIONS:
        raise InstallationRefused(
            f"Unknown installation option {option!r}; use general or full"
        )
    if option is not None and (profile != "general" or supplied_packs):
        raise InstallationRefused(
            "--option cannot be combined with --profile or --packs"
        )

    if option is None and (profile != "general" or supplied_packs):
        return profile, supplied_packs, "custom"

    if interactive is None:
        interactive = sys.stdin.isatty()
    if option is None and interactive:
        counts = install_option_counts(repo_root)
        print(
            "\nYour Installation Options:\n"
            f"  [1] General Profile — installs {counts['agents']} custom agents, "
            f"{counts['workflows']} workflows, and {counts['general_skills']} "
            "General-profile skills. Spatial, Media, and Growth remain dormant.\n"
            f"  [2] Full System — installs {counts['agents']} custom agents, "
            f"{counts['workflows']} workflows, and all {counts['all_skills']} "
            "registered skills, including Spatial, Media, and Growth."
        )
        choice = input("Choose 1 or 2 [1]: ").strip() or "1"
        if choice not in {"1", "2"}:
            raise InstallationRefused("Choose 1 for General or 2 for Full System")
        option = "general" if choice == "1" else "full"

    if option in {None, "general"}:
        return "general", [], "general"

    manifest = load_manifest(repo_root)
    optional_packs = [
        profile_id
        for profile_id in manifest.get("profiles", [])
        if profile_id != "general"
        and manifest.get("profile_definitions", {}).get(profile_id, {}).get("kind")
        == "pack"
    ]
    return "general", optional_packs, "full"


def profile_key(active_packs: Iterable[str]) -> str:
    packs = tuple(active_packs)
    return "general" if not packs else "+".join(packs)


def agent_skills_for_profiles(metadata: dict[str, Any], selected_profiles: Iterable[str]) -> list[str]:
    """Return baseline skills plus profile-specific skills without duplicate loading."""
    active_profiles = set(selected_profiles)
    selected: list[str] = []
    for skill_id in metadata["skills"]:
        if skill_id not in selected:
            selected.append(skill_id)
    for selection in metadata.get("conditional_skills", []):
        if not active_profiles.intersection(selection["profiles"]):
            continue
        for skill_id in selection["skills"]:
            if skill_id not in selected:
                selected.append(skill_id)
    return selected


def render_antigravity_agent(
    source: Path,
    destination: Path,
    adapter: dict[str, Any],
    available_skills: set[str],
    selected_skills: list[str],
) -> None:
    """Render one portable role contract into Antigravity's Markdown agent format."""
    metadata, body = split_frontmatter(source)
    missing_skills = sorted(set(selected_skills) - available_skills)
    if missing_skills:
        raise ValidationFailed(
            f"Agent {metadata['id']} references unavailable skills: {', '.join(missing_skills)}"
        )
    tool_map = adapter["agent_tool_map"]
    tools: list[str] = []
    for capability in metadata["tool_capabilities"]:
        host_tool = tool_map[capability]
        if host_tool not in tools:
            tools.append(host_tool)
    lines = [
        "---",
        f"name: {metadata['name']}",
        f"description: {json.dumps(metadata['description'])}",
        "tools:",
        *(f"  - {tool}" for tool in tools),
        f"mainAgent: {str(metadata['primary_agent']).lower()}",
        f"subagent: {str(metadata['subagent']).lower()}",
        f"model: {metadata['model_tier']}",
        f"commandExecutionPolicy: {metadata['command_policy']}",
        "---",
        "",
    ]
    # Antigravity's Manager surface can discover a workspace agent while leaving
    # its AgentBasePath unset. In that state the documented relative `skills:`
    # frontmatter entries are silently discarded. Workspace skills are still
    # discovered normally, so expose this role's deliberate routes in its prompt
    # rather than making an unusable frontmatter binding.
    capability_routes = [
        "\n\n## Available capability routes\n",
        "The active profile makes these skill guides available to this role:",
        *(f"- `{skill_id}`" for skill_id in selected_skills),
        "",
        "A listed skill is available for analysis, planning, and local drafting. "
        "It does not grant an external account, provider, paid action, publication, "
        "or production change.",
    ]
    capability_routes.extend(
        [
            "",
            "## Required specialist return",
            "Return all of these fields before handoff:",
            *(f"- **{item}**" for item in metadata["return_contract"]),
            "",
            "## Delegation contract",
            *(f"- {item}" for item in metadata["delegation_contract"]),
        ]
    )
    if "video-generation" in selected_skills:
        capability_routes.extend(
            [
                "",
                "`video-generation` is available for video planning, provider-aware "
                "briefing, prompt drafting, comparison, and diagnosis. Direct video "
                "generation remains unavailable unless a visible provider surface, "
                "account access, and just-in-time approval are present.",
            ]
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        "\n".join(lines) + body.lstrip("\n") + "\n".join(capability_routes) + "\n",
        encoding="utf-8",
    )


def render_codex_agent_reference(
    source: Path,
    destination: Path,
    available_skills: set[str],
    selected_skills: list[str],
) -> None:
    """Render a profile-filtered role reference without claiming Codex custom-agent support."""
    metadata, body = split_frontmatter(source)
    missing_skills = sorted(set(selected_skills) - available_skills)
    if missing_skills:
        raise ValidationFailed(
            f"Agent {metadata['id']} references unavailable skills: {', '.join(missing_skills)}"
        )
    routes = [
        "## Available capability routes",
        "",
        "Select only the route that matches the task. These are references, not authority.",
        *(f"- `skills/{skill_id}/SKILL.md`" for skill_id in selected_skills),
        "",
        "## Required specialist return",
        "Return all of these fields before handoff:",
        *(f"- **{item}**" for item in metadata["return_contract"]),
        "",
        "## Delegation contract",
        *(f"- {item}" for item in metadata["delegation_contract"]),
    ]
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        "\n".join(
            [
                "<!-- Generated portable role reference for Codex.",
                "The host's main AGENTS.md policy remains authoritative; this file does not claim host-selectable custom-agent support. -->",
                "",
                body.lstrip("\n").rstrip(),
                "",
                *routes,
                "",
            ]
        ),
        encoding="utf-8",
    )


def activate_staged_payload(stage: Path, final: Path) -> None:
    """Replace a generated payload without deleting the last known-good copy first."""
    backup = final.parent / f".{final.name}-previous-{uuid.uuid4().hex[:8]}"
    moved_existing = False
    try:
        if final.exists():
            final.replace(backup)
            moved_existing = True
        stage.replace(final)
    except Exception:
        if moved_existing and backup.exists() and not final.exists():
            backup.replace(final)
        raise
    if moved_existing:
        shutil.rmtree(backup, ignore_errors=True)


def build_payload(
    host: str,
    profile: str = "general",
    packs: Iterable[str] = (),
    repo_root: Path = REPO_ROOT,
    output_root: Path | None = None,
) -> Path:
    if host not in SUPPORTED_HOSTS:
        raise AntiGravityError(f"Unsupported host: {host}")
    validation = validate_repository(repo_root)
    if not validation["ok"]:
        raise ValidationFailed(
            f"Canonical source has {validation['issue_count']} validation issue(s); run validate"
        )
    manifest = load_manifest(repo_root)
    selected_profiles, active_packs = resolve_pack_selection(manifest, profile, packs)
    adapter = load_json(repo_root / "global" / "adapters" / host / "adapter.json")
    output_root = (output_root or repo_root / "dist").resolve()
    output_root.mkdir(parents=True, exist_ok=True)
    composition_key = profile_key(active_packs)
    host_output = output_root / host
    host_output.mkdir(parents=True, exist_ok=True)
    final = host_output / composition_key
    # Keep the sibling stage name short. Deep skill/reference trees can otherwise
    # cross the legacy Windows MAX_PATH boundary before atomic activation.
    stage = host_output / f".{composition_key}-{uuid.uuid4().hex[:8]}"
    stage.mkdir(parents=True)
    try:
        instruction_source = repo_root / manifest["canonical"]["policy"]
        instruction_target = stage / adapter["instruction_target"]
        instruction_target.parent.mkdir(parents=True, exist_ok=True)
        header = (
            f"<!-- Generated for {host} from canonical Anti-Gravity policy. "
            "Host authority and approval controls remain authoritative. -->\n\n"
        )
        instruction_target.write_text(
            header + instruction_source.read_text(encoding="utf-8-sig"),
            encoding="utf-8",
        )
        content_root = stage / adapter["content_root"]
        content_root.mkdir(parents=True, exist_ok=True)
        copy_entry(
            repo_root / "global" / "GLOBAL_MEMORY.md", content_root / "GLOBAL_MEMORY.md"
        )
        if (repo_root / "global" / "USER_PROFILE.md").exists():
            copy_entry(repo_root / "global" / "USER_PROFILE.md", stage / "USER_PROFILE.md")
        copy_entry(repo_root / "global" / "core", content_root / "core")
        copy_entry(repo_root / "global" / "memory", content_root / "memory")
        copy_entry(repo_root / "global" / "schemas", content_root / "schemas")

        registry_destinations = {
            "skills": Path(adapter["skills_target"]),
            "workflows": Path(adapter["workflows_target"]),
            "context_templates": Path("context_templates"),
            "baselines": Path("baselines"),
            "templates": Path("global_templates"),
            "resources": Path("."),
        }
        for registry_name, destination_root in registry_destinations.items():
            for entry in manifest[registry_name]:
                if not set(selected_profiles).intersection(entry["profiles"]):
                    continue
                source = repo_root / entry["path"]
                if registry_name == "skills":
                    destination = content_root / destination_root / entry["id"]
                elif registry_name == "resources":
                    destination = content_root / entry.get("destination", source.name)
                else:
                    destination = content_root / destination_root / source.name
                copy_entry(source, destination)

        if adapter.get("agent_format") == "antigravity-markdown":
            agent_root = content_root / adapter["agents_target"]
            available_skills = {
                entry["id"]
                for entry in manifest["skills"]
                if set(selected_profiles).intersection(entry["profiles"])
            }
            for entry in manifest["agents"]:
                if host not in entry["host_compatibility"]:
                    continue
                if not set(selected_profiles).intersection(entry["profiles"]):
                    continue
                source = repo_root / entry["path"] / "AGENT.md"
                metadata, _ = split_frontmatter(source)
                render_antigravity_agent(
                    source,
                    agent_root / entry["id"] / "agent.md",
                    adapter,
                    available_skills,
                    agent_skills_for_profiles(metadata, selected_profiles),
                )
        elif host == "codex":
            # Codex does not expose the same host-selectable custom-agent format
            # as Antigravity. Ship profile-filtered role references for the main
            # Codex policy to consult without representing them as native agents.
            agent_root = content_root / "agents"
            available_skills = {
                entry["id"]
                for entry in manifest["skills"]
                if set(selected_profiles).intersection(entry["profiles"])
            }
            for entry in manifest["agents"]:
                if host not in entry["host_compatibility"]:
                    continue
                if not set(selected_profiles).intersection(entry["profiles"]):
                    continue
                source = repo_root / entry["path"] / "AGENT.md"
                metadata, _ = split_frontmatter(source)
                render_codex_agent_reference(
                    source,
                    agent_root / entry["id"] / "agent.md",
                    available_skills,
                    agent_skills_for_profiles(metadata, selected_profiles),
                )

        copy_entry(repo_root / "global" / "manifest.yaml", stage / "manifest.json")
        copy_entry(
            repo_root / "global" / "adapters" / host / "adapter.json",
            stage / "adapter.json",
        )
        write_json_atomic(
            stage / "profile.json",
            {
                "schema_version": 2,
                "base_profile": "general",
                "active_packs": list(active_packs),
                "profile_key": composition_key,
            },
        )
        payload_problems = validate_payload(stage)
        if payload_problems:
            summary = "; ".join(
                f"{problem['path']}: {problem['message']}" for problem in payload_problems[:10]
            )
            raise ValidationFailed(
                f"Generated {host}/{profile} payload has {len(payload_problems)} issue(s): {summary}"
            )
        activate_staged_payload(stage, final)
        return final
    except Exception:
        shutil.rmtree(stage, ignore_errors=True)
        raise


def resolve_install_root(target: Path) -> Path:
    base = target.expanduser().resolve()
    home = Path.home().resolve()
    anchor = Path(base.anchor).resolve()
    if base in {home, anchor}:
        raise InstallationRefused(
            "Refusing a home or filesystem-root target; select a host configuration directory"
        )
    if base.name.lower() == "antigravity":
        install_root = base
    else:
        install_root = base / "antigravity"
    if install_root == base.parent or not install_root.is_relative_to(base):
        raise InstallationRefused("Resolved namespace escaped the selected target")
    return install_root


def resolve_antigravity_global_home(target: Path) -> Path:
    """Validate the native Antigravity global customization root."""
    raw = target.expanduser()
    # Check the user-supplied path before resolve(); resolving first would hide
    # a symlink or junction and could redirect the install outside the named
    # .gemini directory.
    probe = raw
    while True:
        if probe.exists():
            _ensure_not_reparse(probe)
        if probe.parent == probe:
            break
        probe = probe.parent
    base = raw.resolve()
    home = Path.home().resolve()
    anchor = Path(base.anchor).resolve()
    if base in {home, anchor}:
        raise InstallationRefused(
            "Refusing a home or filesystem-root target; select the .gemini directory"
        )
    if base.name.lower() != ".gemini":
        raise InstallationRefused(
            "Native Antigravity global installation requires a target ending in .gemini"
        )
    if base.parent == anchor:
        raise InstallationRefused(
            "Refusing to install directly below the filesystem root"
        )
    return base


def directory_digest(directory: Path) -> str:
    """Return a stable digest for a directory's relative files and contents."""
    digest = hashlib.sha256()
    for relative, source in sorted(file_map(directory).items()):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(bytes.fromhex(sha256_file(source)))
    return digest.hexdigest()


def entry_digest(path: Path) -> str:
    """Return the digest used to prove that an entry is still installer-owned."""
    return directory_digest(path) if path.is_dir() else sha256_file(path)


def _ensure_not_reparse(path: Path) -> None:
    if path.is_symlink():
        raise InstallationRefused(f"Refusing symlink target: {path}")
    try:
        attributes = path.stat().st_file_attributes
    except (AttributeError, FileNotFoundError):
        attributes = 0
    if attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
        raise InstallationRefused(f"Refusing reparse-point target: {path}")


def _replace_entry(source: Path, destination: Path) -> None:
    """Atomically move a staged file or directory using Windows-safe paths."""
    os.replace(filesystem_path(source), filesystem_path(destination))


def _remove_entry(path: Path) -> None:
    """Remove a staged/activated entry without following reparse points."""
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(filesystem_path(path), ignore_errors=True)
    else:
        try:
            os.unlink(filesystem_path(path))
        except FileNotFoundError:
            pass


def installation_changes(payload: Path, install_root: Path) -> dict[str, list[str]]:
    source_files = file_map(payload)
    target_files = file_map(install_root)
    additions: list[str] = []
    replacements: list[str] = []
    unchanged: list[str] = []
    removals = sorted(set(target_files) - set(source_files))
    for relative, source in sorted(source_files.items()):
        target = target_files.get(relative)
        if target is None:
            additions.append(relative)
        elif sha256_file(source) == sha256_file(target):
            unchanged.append(relative)
        else:
            replacements.append(relative)
    return {
        "add": additions,
        "replace": replacements,
        "remove_from_namespace": removals,
        "unchanged": unchanged,
    }


def install_payload(
    payload: Path,
    target: Path,
    host: str,
    dry_run: bool,
    assume_yes: bool,
) -> dict[str, Any]:
    payload = payload.resolve()
    if not payload.is_dir():
        raise InstallationRefused(f"Payload does not exist: {payload}")
    if host not in SUPPORTED_HOSTS:
        raise InstallationRefused(f"Unsupported host: {host}")
    install_root = resolve_install_root(target)
    changes = installation_changes(payload, install_root)
    result: dict[str, Any] = {
        "status": "dry-run" if dry_run else "pending",
        "host": host,
        "target": str(install_root),
        "changes": changes,
        "backup": None,
    }
    if dry_run:
        return result
    if not assume_yes:
        raise InstallationRefused(
            "Installation requires explicit confirmation; rerun with --yes after reviewing --dry-run"
        )

    parent = install_root.parent
    parent.mkdir(parents=True, exist_ok=True)
    stage = parent / f".antigravity-stage-{uuid.uuid4().hex}"
    backup_root = parent / ".antigravity-backups"
    backup = backup_root / utc_timestamp()
    activated_existing = False
    try:
        shutil.copytree(payload, stage)
        if install_root.exists():
            backup_root.mkdir(parents=True, exist_ok=True)
            install_root.replace(backup)
            activated_existing = True
            result["backup"] = str(backup)
        stage.replace(install_root)
        result["status"] = "installed"
        return result
    except Exception:
        shutil.rmtree(stage, ignore_errors=True)
        if activated_existing and backup.exists() and not install_root.exists():
            backup.replace(install_root)
        raise


def antigravity_global_file_map(
    payload: Path,
    gemini_home: Path,
    adapter: dict[str, Any],
) -> dict[Path, Path]:
    """Map a generated Antigravity payload to native global discovery paths."""
    global_install = adapter.get("global_install")
    if not isinstance(global_install, dict):
        raise InstallationRefused(
            "Antigravity adapter does not declare native global installation targets"
        )

    mapping: dict[Path, Path] = {}

    def add(source: Path, target: Path) -> None:
        if not source.exists():
            return
        if target in mapping.values():
            raise InstallationRefused(f"Duplicate Antigravity global target: {target}")
        mapping[source] = target

    add(
        payload / adapter["instruction_target"],
        gemini_home / global_install["instruction_target"],
    )
    add(
        payload / adapter["content_root"] / "GLOBAL_MEMORY.md",
        gemini_home / global_install["router_target"],
    )
    add(
        payload / "USER_PROFILE.md",
        gemini_home / global_install["user_profile_target"],
    )

    content_root = payload / adapter["content_root"]
    for source_name, target_name in (
        ("skills", "skills_target"),
        ("workflows", "workflows_target"),
        ("agents", "agents_target"),
    ):
        source_root = content_root / adapter[f"{source_name}_target"]
        target_root = gemini_home / global_install[target_name]
        if not source_root.exists():
            continue
        for source in sorted(source_root.iterdir()):
            add(source, target_root / source.name)

    # Do not map the complete generated payload into the global namespace.
    # It contains deep reference trees which can cross Windows path limits and
    # would duplicate the direct skill/workflow registries. The native host
    # discovers those registries from the direct targets above. A shallow
    # installation record is written separately by install_antigravity_global.
    return mapping


def antigravity_global_changes(
    payload: Path,
    gemini_home: Path,
    adapter: dict[str, Any],
) -> dict[str, list[str]]:
    mapping = antigravity_global_file_map(payload, gemini_home, adapter)
    additions: list[str] = []
    replacements: list[str] = []
    unchanged: list[str] = []
    for source, target in mapping.items():
        label = target.relative_to(gemini_home).as_posix()
        if not target.exists():
            additions.append(label)
        elif source.is_file() and target.is_file() and sha256_file(source) == sha256_file(target):
            unchanged.append(label)
        elif source.is_dir() and target.is_dir() and directory_digest(source) == directory_digest(target):
            unchanged.append(label)
        else:
            replacements.append(label)
    global_install = adapter["global_install"]
    managed_namespace = gemini_home / global_install["payload_target"]
    active_record_path = managed_namespace / "active.json"
    current_targets = {
        target.relative_to(gemini_home).as_posix() for target in mapping.values()
    }
    stale_targets: list[str] = []
    if active_record_path.exists():
        active_record = load_json(active_record_path)
        previous_targets = active_record.get("direct_targets")
        if not isinstance(previous_targets, list) or not all(
            isinstance(item, str) for item in previous_targets
        ):
            raise InstallationRefused(
                f"Invalid Antigravity installation record: {active_record_path}"
            )
        previous_digests = active_record.get("direct_digests", {})
        if not isinstance(previous_digests, dict) or not all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in previous_digests.items()
        ):
            raise InstallationRefused(
                f"Invalid Antigravity ownership record: {active_record_path}"
            )
        # Only prune entries that the installer previously owned in its own
        # registries. Unrelated global skills, workflows, and agents are never
        # inferred or removed.
        managed_prefixes = ("config/skills/", "config/workflows/", "config/agents/")
        stale_targets = sorted(
            item
            for item in previous_targets
            if item not in current_targets
            and item.startswith(managed_prefixes)
            and (gemini_home / Path(item)).exists()
            and previous_digests.get(item) == entry_digest(gemini_home / Path(item))
        )
    return {
        "add": sorted(additions),
        "replace": sorted(replacements),
        "remove": stale_targets,
        "unchanged": sorted(unchanged),
    }


def install_antigravity_global(
    payload: Path,
    target: Path,
    dry_run: bool,
    assume_yes: bool,
) -> dict[str, Any]:
    """Install only V4-owned files into Antigravity's native global locations."""
    payload = payload.resolve()
    if not payload.is_dir():
        raise InstallationRefused(f"Payload does not exist: {payload}")
    adapter = load_json(payload / "adapter.json")
    if adapter.get("host") != "antigravity":
        raise InstallationRefused("Native global installation requires an antigravity payload")
    gemini_home = resolve_antigravity_global_home(target)
    mapping = antigravity_global_file_map(payload, gemini_home, adapter)
    changes = antigravity_global_changes(payload, gemini_home, adapter)
    global_install = adapter["global_install"]
    managed_namespace = gemini_home / global_install["payload_target"]
    active_record_path = managed_namespace / "active.json"
    profile_key = "general"
    profile_path = payload / "profile.json"
    if profile_path.exists():
        profile = load_json(profile_path)
        profile_key = profile.get("profile_key", profile_key)
    managed_profile = managed_namespace / profile_key
    result: dict[str, Any] = {
        "status": "dry-run" if dry_run else "pending",
        "host": "antigravity",
        "target": str(gemini_home),
        "managed_namespace": str(managed_namespace),
        "managed_record": str(managed_profile / "installation.json"),
        "changes": changes,
        "backup": None,
        "direct_discovery": {
            "agents": str(gemini_home / global_install["agents_target"]),
            "skills": str(gemini_home / global_install["skills_target"]),
            "workflows": str(gemini_home / global_install["workflows_target"]),
            "rule": str(gemini_home / global_install["instruction_target"]),
        },
    }
    if dry_run:
        return result
    if not assume_yes:
        raise InstallationRefused(
            "Native Antigravity global installation requires explicit confirmation; "
            "rerun with --yes after reviewing --dry-run"
        )

    backup_root = gemini_home / ".antigravity-backups" / utc_timestamp()
    stage_root = gemini_home / f".antigravity-global-stage-{uuid.uuid4().hex}"
    activated: list[tuple[Path, Path | None]] = []
    try:
        _ensure_not_reparse(gemini_home) if gemini_home.exists() else None
        stage_root.mkdir(parents=True, exist_ok=False)
        staged_pairs: list[tuple[Path, Path]] = []
        unchanged = set(changes["unchanged"])
        for source, destination in mapping.items():
            label = destination.relative_to(gemini_home).as_posix()
            if label in unchanged:
                continue
            if destination.exists():
                _ensure_not_reparse(destination)
            staged = stage_root / destination.relative_to(gemini_home)
            staged.parent.mkdir(parents=True, exist_ok=True)
            copy_entry(source, staged)
            staged_pairs.append((staged, destination))

        for staged, destination in staged_pairs:
            backup_path: Path | None = None
            if destination.exists():
                backup_path = backup_root / destination.relative_to(gemini_home)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                _replace_entry(destination, backup_path)
            destination.parent.mkdir(parents=True, exist_ok=True)
            _replace_entry(staged, destination)
            activated.append((destination, backup_path))

        # Retire only entries recorded by an earlier Anti-Gravity install when
        # switching from Full to General (or another smaller profile). Every
        # retired entry is moved into the same rollback backup; nothing is
        # deleted and unrelated global entries are outside this list.
        for relative in changes.get("remove", []):
            destination = gemini_home / Path(relative)
            if not destination.exists():
                continue
            _ensure_not_reparse(destination)
            backup_path = backup_root / destination.relative_to(gemini_home)
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            _replace_entry(destination, backup_path)
            activated.append((destination, backup_path))

        # Keep only shallow provenance in the managed namespace. The canonical
        # repository remains the source of truth; direct native paths above are
        # what Antigravity discovers. Avoid copying the complete payload here.
        managed_stage = stage_root / "managed" / profile_key
        managed_stage.mkdir(parents=True, exist_ok=True)
        for metadata_name in ("adapter.json", "manifest.json", "profile.json"):
            source = payload / metadata_name
            if source.exists():
                copy_entry(source, managed_stage / metadata_name)
        managed_backup: Path | None = None
        if managed_profile.exists():
            _ensure_not_reparse(managed_profile)
            managed_backup = backup_root / managed_profile.relative_to(gemini_home)
            managed_backup.parent.mkdir(parents=True, exist_ok=True)
            _replace_entry(managed_profile, managed_backup)
        managed_profile.parent.mkdir(parents=True, exist_ok=True)
        _replace_entry(managed_stage, managed_profile)
        activated.append((managed_profile, managed_backup))
        record = {
            "schema_version": 1,
            "host": "antigravity",
            "installed_at": datetime.now(timezone.utc).isoformat(),
            "payload_profile": str(managed_profile.relative_to(managed_namespace)),
            "target": str(gemini_home),
            "direct_targets": sorted(
                str(destination.relative_to(gemini_home)).replace("\\", "/")
                for source, destination in mapping.items()
                if source != payload
            ),
            "direct_digests": {
                str(destination.relative_to(gemini_home)).replace("\\", "/"): entry_digest(
                    destination
                )
                for source, destination in mapping.items()
                if source != payload
            },
            "removed_targets": list(changes.get("remove", [])),
            "active_record": str(active_record_path),
            "backup": str(backup_root) if backup_root.exists() else None,
        }
        write_json_atomic(managed_profile / "installation.json", record)

        active_stage = stage_root / "managed" / "active.json"
        write_json_atomic(active_stage, record)
        active_backup: Path | None = None
        if active_record_path.exists():
            _ensure_not_reparse(active_record_path)
            active_backup = backup_root / active_record_path.relative_to(gemini_home)
            active_backup.parent.mkdir(parents=True, exist_ok=True)
            _replace_entry(active_record_path, active_backup)
        active_record_path.parent.mkdir(parents=True, exist_ok=True)
        _replace_entry(active_stage, active_record_path)
        activated.append((active_record_path, active_backup))

        required = [
            gemini_home / global_install["instruction_target"],
            gemini_home / global_install["router_target"],
        ]
        required.extend(
            destination / "agent.md"
            for source, destination in mapping.items()
            if source.parent.name == adapter["agents_target"]
        )
        missing = [str(path) for path in required if not path.exists()]
        if missing:
            raise InstallationRefused(
                "Post-install validation failed; missing: " + ", ".join(missing)
            )
        shutil.rmtree(filesystem_path(stage_root), ignore_errors=True)
        result["backup"] = str(backup_root) if backup_root.exists() else None
        result["status"] = "installed"
        return result
    except Exception:
        for destination, backup_path in reversed(activated):
            if destination.exists():
                _remove_entry(destination)
            if backup_path and backup_path.exists():
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                _replace_entry(backup_path, destination)
        shutil.rmtree(filesystem_path(stage_root), ignore_errors=True)
        raise


def resolve_codex_home(target: Path) -> Path:
    """Validate a Codex home for direct global instruction integration."""
    base = target.expanduser().resolve()
    home = Path.home().resolve()
    anchor = Path(base.anchor).resolve()
    if base in {home, anchor}:
        raise InstallationRefused(
            "Refusing a home or filesystem-root Codex target; select the Codex home directory"
        )
    if base.name.lower() != ".codex" and not (base / "config.toml").exists():
        raise InstallationRefused(
            "Direct Codex integration requires an existing .codex/CODEX_HOME directory"
        )
    if not base.is_relative_to(base.anchor):
        raise InstallationRefused("Resolved Codex home escaped its filesystem anchor")
    return base


def codex_global_file_map(payload: Path, codex_home: Path) -> dict[Path, Path]:
    """Return only the explicit Codex discovery files/directories to replace."""
    mapping: dict[Path, Path] = {}
    for source_name, target_name in (
        (Path("AGENTS.md"), Path("AGENTS.md")),
        (Path("USER_PROFILE.md"), Path("USER_PROFILE.md")),
        (Path(".agents") / "GLOBAL_MEMORY.md", Path("GLOBAL_MEMORY.md")),
    ):
        source = payload / source_name
        if source.exists():
            mapping[source] = codex_home / target_name
    for source_root, target_root in (
        (payload / ".agents" / "skills", codex_home / "skills"),
        (payload / ".agents" / "workflows", codex_home / "workflows"),
    ):
        if not source_root.exists():
            continue
        for source in sorted(source_root.iterdir()):
            mapping[source] = target_root / source.name
    return mapping


def codex_global_changes(payload: Path, codex_home: Path) -> dict[str, list[str]]:
    mapping = codex_global_file_map(payload, codex_home)
    additions: list[str] = []
    replacements: list[str] = []
    unchanged: list[str] = []
    for source, target in mapping.items():
        label = str(target.relative_to(codex_home))
        if not target.exists():
            additions.append(label)
        elif source.is_file() and target.is_file() and sha256_file(source) == sha256_file(target):
            unchanged.append(label)
        else:
            replacements.append(label)
    return {"add": additions, "replace": replacements, "unchanged": unchanged}


def install_codex_global(
    payload: Path,
    target: Path,
    dry_run: bool,
    assume_yes: bool,
) -> dict[str, Any]:
    """Install generated Codex instructions while preserving unrelated Codex state."""
    payload = payload.resolve()
    codex_home = resolve_codex_home(target)
    mapping = codex_global_file_map(payload, codex_home)
    changes = codex_global_changes(payload, codex_home)
    result: dict[str, Any] = {
        "status": "dry-run" if dry_run else "pending",
        "host": "codex",
        "target": str(codex_home),
        "changes": changes,
        "namespace": str(codex_home / "antigravity"),
        "backup": None,
    }
    if dry_run:
        return result
    if not assume_yes:
        raise InstallationRefused(
            "Direct Codex integration requires explicit confirmation; rerun with --yes after reviewing --dry-run"
        )

    timestamp = utc_timestamp()
    backup_root = codex_home / ".antigravity-backups" / timestamp
    stage_root = codex_home / f".antigravity-codex-stage-{uuid.uuid4().hex}"
    namespace_source = stage_root / "namespace"
    activated: list[tuple[Path, Path]] = []
    try:
        shutil.copytree(payload, namespace_source)
        for source, target_path in mapping.items():
            staged = stage_root / "direct" / target_path.relative_to(codex_home)
            if source.is_dir():
                shutil.copytree(source, staged)
            else:
                staged.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, staged)
        for source, target_path in mapping.items():
            if target_path.exists():
                backup_path = backup_root / target_path.relative_to(codex_home)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                target_path.replace(backup_path)
            staged = stage_root / "direct" / target_path.relative_to(codex_home)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            staged.replace(target_path)
            activated.append((target_path, backup_root / target_path.relative_to(codex_home)))
        namespace_target = codex_home / "antigravity"
        if namespace_target.exists():
            namespace_backup = backup_root / "antigravity"
            namespace_backup.parent.mkdir(parents=True, exist_ok=True)
            namespace_target.replace(namespace_backup)
        namespace_source.replace(namespace_target)
        record = {
            "schema_version": 1,
            "host": "codex",
            "installed_at": datetime.now(timezone.utc).isoformat(),
            "payload": str(payload),
            "codex_home": str(codex_home),
            "backup": str(backup_root),
            "direct_targets": sorted(changes["add"] + changes["replace"]),
        }
        write_json_atomic(namespace_target / "installation.json", record)
        result["backup"] = str(backup_root) if backup_root.exists() else None
        result["status"] = "installed"
        return result
    except Exception:
        for target_path, backup_path in reversed(activated):
            if target_path.exists():
                if target_path.is_dir():
                    shutil.rmtree(target_path)
                else:
                    target_path.unlink()
            if backup_path.exists():
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                backup_path.replace(target_path)
        shutil.rmtree(stage_root, ignore_errors=True)
        raise


def print_validation(result: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(result, indent=2))
        return
    if result["ok"]:
        print("Anti-Gravity OS validation passed.")
        return
    print(f"Anti-Gravity OS validation found {result['issue_count']} issue(s):")
    for problem in result["issues"]:
        print(f"- [{problem['code']}] {problem['path']}: {problem['message']}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Anti-Gravity OS development CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="Validate canonical source")
    validate_parser.add_argument("--json", action="store_true", help="Emit JSON")

    build_parser_command = subparsers.add_parser("build", help="Build a host payload")
    build_parser_command.add_argument("--host", required=True, choices=SUPPORTED_HOSTS)
    build_parser_command.add_argument(
        "--profile",
        default="general",
        help="Backward-compatible single optional pack shorthand",
    )
    build_parser_command.add_argument(
        "--packs",
        action="append",
        default=[],
        help="Comma-separated optional packs; may be repeated",
    )
    build_parser_command.add_argument("--output", type=Path)

    install_parser = subparsers.add_parser("install", help="Safely install a host payload")
    install_parser.add_argument("--host", required=True, choices=SUPPORTED_HOSTS)
    install_parser.add_argument(
        "--profile",
        default="general",
        help="Backward-compatible single optional pack shorthand",
    )
    install_parser.add_argument(
        "--packs",
        action="append",
        default=[],
        help="Comma-separated optional packs; may be repeated",
    )
    install_parser.add_argument(
        "--option",
        choices=INSTALL_OPTIONS,
        help="Installation choice; omit in a terminal to be asked General or Full",
    )
    install_parser.add_argument("--target", required=True, type=Path)
    install_parser.add_argument("--dry-run", action="store_true")
    install_parser.add_argument("--yes", action="store_true")
    install_parser.add_argument(
        "--codex-global",
        action="store_true",
        help="For host=codex, install into Codex discovery locations plus a rollback namespace",
    )
    install_parser.add_argument(
        "--antigravity-global",
        action="store_true",
        help="For host=antigravity, install into native global discovery locations plus a rollback namespace",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = build_parser().parse_args(argv)
    try:
        if args.command == "validate":
            result = validate_repository()
            print_validation(result, args.json)
            return 0 if result["ok"] else 1
        if args.command == "build":
            payload = build_payload(args.host, args.profile, args.packs, output_root=args.output)
            print(json.dumps({"status": "built", "payload": str(payload)}, indent=2))
            return 0
        if args.command == "install":
            if args.codex_global and args.host != "codex":
                raise InstallationRefused("--codex-global is only valid with --host codex")
            if args.antigravity_global and args.host != "antigravity":
                raise InstallationRefused(
                    "--antigravity-global is only valid with --host antigravity"
                )
            if args.codex_global and args.antigravity_global:
                raise InstallationRefused(
                    "Choose only one host-specific global installation mode"
                )
            selected_profile, selected_packs, selected_option = resolve_install_option(
                REPO_ROOT,
                args.option,
                args.profile,
                args.packs,
            )
            if args.dry_run:
                with tempfile.TemporaryDirectory(prefix="antigravity-dry-run-") as directory:
                    payload = build_payload(
                        args.host,
                        selected_profile,
                        selected_packs,
                        output_root=Path(directory),
                    )
                    result = (
                        install_codex_global(payload, args.target, True, False)
                        if args.codex_global
                        else install_antigravity_global(payload, args.target, True, False)
                        if args.antigravity_global
                        else install_payload(payload, args.target, args.host, True, False)
                    )
            else:
                payload = build_payload(args.host, selected_profile, selected_packs)
                result = (
                    install_codex_global(payload, args.target, False, args.yes)
                    if args.codex_global
                    else install_antigravity_global(payload, args.target, False, args.yes)
                    if args.antigravity_global
                    else install_payload(payload, args.target, args.host, False, args.yes)
                )
            result["installation_option"] = selected_option
            print(json.dumps(result, indent=2))
            return 0
    except AntiGravityError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
