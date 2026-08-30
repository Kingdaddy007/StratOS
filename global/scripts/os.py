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
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any, Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
GLOBAL_ROOT = REPO_ROOT / "global"
MANIFEST_PATH = GLOBAL_ROOT / "manifest.yaml"
SUPPORTED_HOSTS = ("antigravity", "gemini", "codex", "cursor", "windsurf", "opencode", "zed")
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
    "invoke_agent",
    "define_worker",
    "message_agent",
    "manage_agents",
}
CANONICAL_AGENT_COLLABORATION_CAPABILITIES = {
    "invoke_agent",
    "define_worker",
    "message_agent",
    "manage_agents",
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


def validate_acceptance_gates(state: dict[str, Any]) -> None:
    """Validate optional acceptance gates without executing their procedures."""
    if "acceptance_gates" not in state:
        return
    gates = state["acceptance_gates"]
    if not isinstance(gates, list):
        raise ValueError("acceptance_gates must be an array")

    required_fields = {
        "id",
        "claim",
        "owner",
        "required",
        "status",
        "depends_on",
        "verification",
        "evidence",
        "limitations",
        "blocker",
        "waiver",
    }
    verification_fields = {"kind", "procedure", "success_condition"}
    valid_statuses = {"pending", "met", "blocked", "waived"}
    valid_kinds = {"command", "test", "inspection", "review"}
    gates_by_id: dict[str, dict[str, Any]] = {}

    for position, gate in enumerate(gates):
        if not isinstance(gate, dict):
            raise ValueError(f"acceptance_gates[{position}] must be an object")
        missing = required_fields - set(gate)
        unknown = set(gate) - required_fields
        if missing:
            raise ValueError(
                f"acceptance_gates[{position}] is missing: {', '.join(sorted(missing))}"
            )
        if unknown:
            raise ValueError(
                f"acceptance_gates[{position}] has unknown fields: "
                + ", ".join(sorted(unknown))
            )

        gate_id = gate["id"]
        if not isinstance(gate_id, str) or not re.fullmatch(r"[A-Za-z0-9._-]+", gate_id):
            raise ValueError(
                f"acceptance_gates[{position}].id must contain only letters, digits, dot, underscore, or hyphen"
            )
        if gate_id in gates_by_id:
            raise ValueError(f"Duplicate acceptance gate id: {gate_id}")
        gates_by_id[gate_id] = gate

        for field in ("claim", "owner"):
            if not isinstance(gate[field], str) or not gate[field].strip():
                raise ValueError(f"acceptance gate {gate_id}.{field} must be a non-empty string")
        if not isinstance(gate["required"], bool):
            raise ValueError(f"acceptance gate {gate_id}.required must be a boolean")
        if gate["status"] not in valid_statuses:
            raise ValueError(f"acceptance gate {gate_id} has unsupported status")

        dependencies = gate["depends_on"]
        if (
            not isinstance(dependencies, list)
            or not all(isinstance(item, str) and re.fullmatch(r"[A-Za-z0-9._-]+", item) for item in dependencies)
            or len(set(dependencies)) != len(dependencies)
        ):
            raise ValueError(
                f"acceptance gate {gate_id}.depends_on must contain unique valid gate ids"
            )

        verification = gate["verification"]
        if not isinstance(verification, dict):
            raise ValueError(f"acceptance gate {gate_id}.verification must be an object")
        missing_verification = verification_fields - set(verification)
        unknown_verification = set(verification) - verification_fields
        if missing_verification or unknown_verification:
            raise ValueError(
                f"acceptance gate {gate_id}.verification must contain exactly "
                "kind, procedure, and success_condition"
            )
        if verification["kind"] not in valid_kinds:
            raise ValueError(f"acceptance gate {gate_id} has unsupported verification kind")
        for field in ("procedure", "success_condition"):
            if not isinstance(verification[field], str) or not verification[field].strip():
                raise ValueError(
                    f"acceptance gate {gate_id}.verification.{field} must be a non-empty string"
                )

        evidence = gate["evidence"]
        if not isinstance(evidence, list) or not all(isinstance(item, dict) for item in evidence):
            raise ValueError(f"acceptance gate {gate_id}.evidence must be an array of objects")
        evidence_fields = {"result", "source", "observed_at"}
        for evidence_position, item in enumerate(evidence):
            if "result" not in item or set(item) - evidence_fields:
                raise ValueError(
                    f"acceptance gate {gate_id}.evidence[{evidence_position}] must contain "
                    "result and may contain only source and observed_at"
                )
            if not all(isinstance(value, str) and value.strip() for value in item.values()):
                raise ValueError(
                    f"acceptance gate {gate_id}.evidence[{evidence_position}] values must be non-empty strings"
                )
            observed_at = item.get("observed_at")
            if observed_at is not None:
                try:
                    observed_time = datetime.fromisoformat(observed_at.replace("Z", "+00:00"))
                except ValueError as error:
                    raise ValueError(
                        f"acceptance gate {gate_id}.evidence[{evidence_position}].observed_at "
                        "must be an ISO 8601 timestamp"
                    ) from error
                if observed_time.tzinfo is None:
                    raise ValueError(
                        f"acceptance gate {gate_id}.evidence[{evidence_position}].observed_at "
                        "must include a timezone"
                    )
        limitations = gate["limitations"]
        if not isinstance(limitations, list) or not all(
            isinstance(item, str) for item in limitations
        ):
            raise ValueError(f"acceptance gate {gate_id}.limitations must be an array of strings")
        blocker = gate["blocker"]
        if blocker is not None and (not isinstance(blocker, str) or not blocker.strip()):
            raise ValueError(f"acceptance gate {gate_id}.blocker must be null or non-empty")

        waiver = gate["waiver"]
        if waiver is not None:
            if not isinstance(waiver, dict) or set(waiver) != {"reason", "approved_by"}:
                raise ValueError(
                    f"acceptance gate {gate_id}.waiver must contain reason and approved_by"
                )
            if not all(isinstance(value, str) and value.strip() for value in waiver.values()):
                raise ValueError(f"acceptance gate {gate_id}.waiver values must be non-empty")

        status = gate["status"]
        if status == "met" and not evidence:
            raise ValueError(f"acceptance gate {gate_id} cannot be met without evidence")
        if status == "blocked" and blocker is None:
            raise ValueError(f"acceptance gate {gate_id} cannot be blocked without a blocker")
        if status != "blocked" and blocker is not None:
            raise ValueError(f"acceptance gate {gate_id} has a blocker but is not blocked")
        if status == "waived":
            if gate["required"]:
                raise ValueError(f"Required acceptance gate {gate_id} cannot be waived")
            if waiver is None:
                raise ValueError(f"acceptance gate {gate_id} cannot be waived without approval")
        elif waiver is not None:
            raise ValueError(f"acceptance gate {gate_id} has a waiver but is not waived")

    for gate_id, gate in gates_by_id.items():
        for dependency in gate["depends_on"]:
            if dependency not in gates_by_id:
                raise ValueError(
                    f"acceptance gate {gate_id} depends on unknown gate {dependency}"
                )
            if dependency == gate_id:
                raise ValueError(f"acceptance gate {gate_id} cannot depend on itself")

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(gate_id: str) -> None:
        if gate_id in visiting:
            raise ValueError("acceptance_gates dependencies must be acyclic")
        if gate_id in visited:
            return
        visiting.add(gate_id)
        for dependency in gates_by_id[gate_id]["depends_on"]:
            visit(dependency)
        visiting.remove(gate_id)
        visited.add(gate_id)

    for gate_id in gates_by_id:
        visit(gate_id)

    for gate_id, gate in gates_by_id.items():
        if gate["status"] != "met":
            continue
        unresolved_dependencies = [
            dependency
            for dependency in gate["depends_on"]
            if gates_by_id[dependency]["status"] != "met"
        ]
        if unresolved_dependencies:
            raise ValueError(
                f"acceptance gate {gate_id} cannot be met before its dependencies: "
                + ", ".join(unresolved_dependencies)
            )

    if state.get("status") == "complete":
        unresolved = [
            gate_id
            for gate_id, gate in gates_by_id.items()
            if gate["status"] not in {"met", "waived"}
        ]
        if unresolved:
            raise ValueError(
                "A complete workflow state cannot contain unresolved acceptance gates: "
                + ", ".join(unresolved)
            )


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
    validate_acceptance_gates(state)

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
        tool_capabilities = set(metadata.get("tool_capabilities", []))
        if any(value not in CANONICAL_AGENT_TOOL_CAPABILITIES for value in tool_capabilities):
            problems.append(issue("agent-tools", relative, "unknown canonical tool capability"))
        if metadata.get("model_tier") not in {"inherit", "flash", "pro"}:
            problems.append(issue("agent-model", relative, "invalid model_tier"))
        if metadata.get("command_policy") not in {"off", "sandbox"}:
            problems.append(issue("agent-command-policy", relative, "invalid command_policy"))
        for field in ("primary_agent", "subagent", "can_delegate"):
            if not isinstance(metadata.get(field), bool):
                problems.append(issue("agent-field-type", relative, f"{field} must be boolean"))
        if metadata.get("can_delegate") is True:
            missing_collaboration = (
                CANONICAL_AGENT_COLLABORATION_CAPABILITIES - tool_capabilities
            )
            if missing_collaboration:
                problems.append(
                    issue(
                        "agent-delegation-tools",
                        relative,
                        "can_delegate requires: "
                        + ", ".join(sorted(missing_collaboration)),
                    )
                )
        elif tool_capabilities.intersection(
            CANONICAL_AGENT_COLLABORATION_CAPABILITIES
        ):
            problems.append(
                issue(
                    "agent-delegation-tools",
                    relative,
                    "collaboration capabilities require can_delegate: true",
                )
            )
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
            workspace_install = adapter.get("workspace_install")
            if not isinstance(workspace_install, dict):
                problems.append(
                    issue(
                        "adapter-workspace-install",
                        path.relative_to(repo_root),
                        "antigravity adapter must declare workspace_install targets",
                    )
                )
            else:
                missing_workspace_fields = required_global_fields - set(workspace_install)
                if missing_workspace_fields:
                    problems.append(
                        issue(
                            "adapter-workspace-install",
                            path.relative_to(repo_root),
                            f"missing {sorted(missing_workspace_fields)}",
                        )
                    )
        if host == "codex":
            agent_fields = {"agents_target", "agent_format"}
            missing_agent_fields = agent_fields - set(adapter)
            if missing_agent_fields:
                problems.append(
                    issue(
                        "adapter-agents",
                        path.relative_to(repo_root),
                        f"missing {sorted(missing_agent_fields)}",
                    )
                )
            elif adapter.get("agent_format") != "codex-toml":
                problems.append(
                    issue("adapter-agents", path.relative_to(repo_root), "unsupported agent_format")
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


SPECIALIST_WORKFLOW_BOUNDARY = [
    "An assigned workflow or acceptance gate narrows your charter; it does not grant authority.",
    "Return candidate evidence, limitations, and blockers. The accountable parent integrates the result and decides final gate status; you cannot waive a required gate or certify your own completion claim.",
]

ANTIGRAVITY_DELEGATION_BOUNDARY = [
    "You may invoke an installed Custom Agent or define temporary workers only when the delegation test in this contract passes.",
    "A functional lead invoked as a child may create its own bounded workers when the host exposes these tools; every child must report to its immediate parent.",
    "When defining a temporary worker, keep subagent-delegation capability disabled. Workers cannot create children or expand their charter.",
    "Use agent messages and management tools for coordination, interruption, and collection of results; do not treat a child response as accepted evidence until the accountable parent checks it.",
    "A worker created by the implementer may self-check that implementation, but final independent assurance must remain a separate sibling route owned by the Studio Director or user.",
]


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
    if metadata["subagent"]:
        capability_routes.extend(
            [
                "",
                "## Assigned workflow and acceptance gate",
                *SPECIALIST_WORKFLOW_BOUNDARY,
            ]
        )
    if metadata["can_delegate"]:
        capability_routes.extend(
            [
                "",
                "## Host-enabled delegation",
                *(f"- {item}" for item in ANTIGRAVITY_DELEGATION_BOUNDARY),
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


def render_codex_agent_toml(
    source: Path,
    destination: Path,
    available_skills: set[str],
    selected_skills: list[str],
) -> None:
    """Render one bounded specialist contract as a native Codex custom agent."""
    metadata, body = split_frontmatter(source)
    if not metadata["subagent"]:
        raise ValidationFailed(f"Codex custom agent {metadata['id']} is not a subagent role")
    missing_skills = sorted(set(selected_skills) - available_skills)
    if missing_skills:
        raise ValidationFailed(
            f"Agent {metadata['id']} references unavailable skills: {', '.join(missing_skills)}"
        )

    sandbox_mode = (
        "workspace-write"
        if metadata["default_mutation_class"] == "local_edit"
        else "read-only"
    )
    instructions = "\n".join(
        [
            "Generated from the canonical Anti-Gravity V4 role contract.",
            "The parent task, applicable AGENTS.md files, and host safety controls remain authoritative.",
            "You are a bounded specialist, not the task owner. Work only within the parent charter and return the required handoff; do not self-authorize broader scope, external effects, destructive actions, dependencies, or global-policy changes.",
            *SPECIALIST_WORKFLOW_BOUNDARY,
            "",
            body.lstrip("\n").rstrip(),
            "",
            "## Available capability routes",
            "Select only the route that matches the charter. A route is not permission.",
            *(f"- `{skill_id}`" for skill_id in selected_skills),
            "",
            "## Required specialist return",
            *(f"- {item}" for item in metadata["return_contract"]),
            "",
            "## Delegation contract",
            *(f"- {item}" for item in metadata["delegation_contract"]),
        ]
    )
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        "\n".join(
            [
                "# Generated Codex custom agent. Edit the canonical global/agents contract instead.",
                f"name = {json.dumps(metadata['name'])}",
                f"description = {json.dumps(metadata['description'])}",
                f"sandbox_mode = {json.dumps(sandbox_mode)}",
                f"developer_instructions = {json.dumps(instructions)}",
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
        elif adapter.get("agent_format") == "codex-toml":
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
                selected_agent_skills = agent_skills_for_profiles(metadata, selected_profiles)
                if metadata["subagent"]:
                    render_codex_agent_toml(
                        source,
                        agent_root / f"{entry['id']}.toml",
                        available_skills,
                        selected_agent_skills,
                    )
                else:
                    # Codex's main task is governed by AGENTS.md. Keep the Studio
                    # Director contract as a generated reference rather than
                    # misrepresenting it as a spawnable worker.
                    render_codex_agent_reference(
                        source,
                        agent_root / entry["id"] / "agent.md",
                        available_skills,
                        selected_agent_skills,
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
    if hasattr(path, "is_junction") and path.is_junction():
        raise InstallationRefused(f"Refusing reparse-point target: {path}")
    try:
        attributes = path.stat().st_file_attributes
    except (AttributeError, FileNotFoundError):
        attributes = 0
    if attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
        raise InstallationRefused(f"Refusing reparse-point target: {path}")


def _absolute_without_resolving(path: Path) -> Path:
    """Return an absolute lexical path while preserving symlink/junction identity."""
    return Path(os.path.abspath(os.fspath(path.expanduser())))


def ensure_existing_path_chain_not_reparse(path: Path) -> None:
    """Reject any existing symlink or junction from a path through its anchor."""
    probe = _absolute_without_resolving(path)
    while True:
        if probe.exists() or probe.is_symlink():
            _ensure_not_reparse(probe)
        if probe.parent == probe:
            break
        probe = probe.parent


def ensure_workspace_destination(workspace: Path, destination: Path, context: str) -> Path:
    """Validate containment and all existing path components before a workspace write."""
    workspace_root = workspace.resolve()
    lexical_destination = _absolute_without_resolving(destination)
    try:
        relative = lexical_destination.relative_to(workspace_root)
    except ValueError as error:
        raise InstallationRefused(
            f"{context} is outside the selected workspace: {lexical_destination}"
        ) from error

    current = workspace_root
    if current.exists() or current.is_symlink():
        _ensure_not_reparse(current)
    for part in relative.parts:
        current = current / part
        if current.exists() or current.is_symlink():
            _ensure_not_reparse(current)
    if not current.resolve(strict=False).is_relative_to(workspace_root):
        raise InstallationRefused(f"{context} escaped the selected workspace: {current}")
    return current


def workspace_record_target(workspace: Path, label: str, record_path: Path) -> Path:
    """Resolve one installer-owned record label without allowing it to escape."""
    posix_path = PurePosixPath(label)
    windows_path = PureWindowsPath(label)
    normalized = posix_path.as_posix()
    if (
        not label
        or "\x00" in label
        or "\\" in label
        or normalized in {"", "."}
        or normalized != label
        or posix_path.is_absolute()
        or windows_path.is_absolute()
        or bool(windows_path.drive)
        or ".." in posix_path.parts
    ):
        raise InstallationRefused(
            f"Unsafe workspace target in installation record {record_path}: {label!r}"
        )

    destination = workspace.resolve().joinpath(*posix_path.parts)
    return ensure_workspace_destination(
        workspace,
        destination,
        f"Workspace target from installation record {record_path}",
    )


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


def resolve_antigravity_workspace(target: Path) -> Path:
    """Validate one existing project directory for a workspace-scoped install."""
    raw_workspace = _absolute_without_resolving(target)
    ensure_existing_path_chain_not_reparse(raw_workspace)
    workspace = raw_workspace.resolve()
    home = Path.home().resolve()
    anchor = Path(workspace.anchor).resolve()
    if workspace in {home, anchor}:
        raise InstallationRefused(
            "Refusing a home or filesystem-root workspace; select one project directory"
        )
    if not workspace.is_dir():
        raise InstallationRefused(
            "Antigravity workspace installation requires an existing project directory"
        )
    if workspace.name.lower() == ".gemini":
        raise InstallationRefused(
            "Antigravity workspace installation requires a project directory, not GEMINI_HOME"
        )
    if not workspace.is_relative_to(workspace.anchor):
        raise InstallationRefused("Resolved Antigravity workspace escaped its filesystem anchor")
    return workspace


def antigravity_workspace_file_map(
    payload: Path,
    workspace: Path,
    adapter: dict[str, Any],
) -> dict[Path, Path]:
    """Map a generated payload to Antigravity's project discovery locations."""
    workspace_install = adapter.get("workspace_install")
    if not isinstance(workspace_install, dict):
        raise InstallationRefused(
            "Antigravity adapter does not declare native workspace installation targets"
        )
    workspace_root = workspace / workspace_install["root_name"]
    mapping: dict[Path, Path] = {}

    def add(source: Path, destination: Path) -> None:
        if not source.exists():
            return
        if destination in mapping.values():
            raise InstallationRefused(f"Duplicate Antigravity workspace target: {destination}")
        mapping[source] = destination

    # The host probe and current Antigravity migration docs both confirm that a
    # workspace-root GEMINI.md is automatically parsed. The native .agents tree
    # holds project-scoped agents, skills, workflows, and supporting references.
    add(
        payload / adapter["instruction_target"],
        workspace / workspace_install["instruction_target"],
    )
    add(
        payload / "USER_PROFILE.md",
        workspace_root / workspace_install["user_profile_target"],
    )

    content_root = payload / adapter["content_root"]
    if not content_root.is_dir():
        raise InstallationRefused("Antigravity payload is missing its .agents resource tree")
    for source in sorted(content_root.iterdir()):
        if source.is_file():
            add(source, workspace_root / source.name)
            continue
        for child in sorted(source.iterdir()):
            add(child, workspace_root / source.name / child.name)
    return mapping


def antigravity_workspace_record_path(
    workspace: Path,
    adapter: dict[str, Any],
) -> Path:
    workspace_install = adapter["workspace_install"]
    return (
        workspace
        / workspace_install["root_name"]
        / workspace_install["payload_target"]
        / "installation.json"
    )


def antigravity_workspace_changes(
    payload: Path,
    workspace: Path,
    adapter: dict[str, Any],
) -> dict[str, list[str]]:
    """Plan a local install without replacing unmanaged project customizations."""
    mapping = antigravity_workspace_file_map(payload, workspace, adapter)
    record_path = antigravity_workspace_record_path(workspace, adapter)
    previous_targets: set[str] = set()
    previous_digests: dict[str, str] = {}
    previous_paths: dict[str, Path] = {}
    if record_path.exists():
        record = load_json(record_path)
        raw_targets = record.get("direct_targets")
        raw_digests = record.get("direct_digests")
        if not isinstance(raw_targets, list) or not all(
            isinstance(item, str) for item in raw_targets
        ):
            raise InstallationRefused(
                f"Invalid Antigravity workspace installation record: {record_path}"
            )
        if not isinstance(raw_digests, dict) or not all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in raw_digests.items()
        ):
            raise InstallationRefused(
                f"Invalid Antigravity workspace ownership record: {record_path}"
            )
        previous_targets = set(raw_targets)
        previous_digests = raw_digests
        previous_paths = {
            label: workspace_record_target(workspace, label, record_path)
            for label in previous_targets | set(previous_digests)
        }

    additions: list[str] = []
    replacements: list[str] = []
    unchanged: list[str] = []
    for source, destination in mapping.items():
        destination = ensure_workspace_destination(
            workspace, destination, "Antigravity workspace target"
        )
        label = destination.relative_to(workspace).as_posix()
        if not destination.exists():
            additions.append(label)
        elif entry_digest(source) == entry_digest(destination):
            unchanged.append(label)
        elif label in previous_targets and previous_digests.get(label) == entry_digest(destination):
            replacements.append(label)
        else:
            raise InstallationRefused(
                "Refusing to replace unmanaged or locally modified Antigravity workspace entry: "
                f"{label}. Choose a clean workspace or remove the conflicting entry yourself."
            )

    current_targets = {
        destination.relative_to(workspace).as_posix() for destination in mapping.values()
    }
    stale_targets = sorted(
        label
        for label in previous_targets - current_targets
        if previous_paths[label].exists()
        and previous_digests.get(label) == entry_digest(previous_paths[label])
    )
    return {
        "add": sorted(additions),
        "replace": sorted(replacements),
        "remove": stale_targets,
        "unchanged": sorted(unchanged),
    }


def install_antigravity_workspace(
    payload: Path,
    target: Path,
    dry_run: bool,
    assume_yes: bool,
) -> dict[str, Any]:
    """Install V4 into one Antigravity project without changing GEMINI_HOME."""
    payload = payload.resolve()
    if not payload.is_dir():
        raise InstallationRefused(f"Payload does not exist: {payload}")
    adapter = load_json(payload / "adapter.json")
    if adapter.get("host") != "antigravity":
        raise InstallationRefused(
            "Antigravity workspace installation requires an antigravity payload"
        )
    workspace = resolve_antigravity_workspace(target)
    mapping = antigravity_workspace_file_map(payload, workspace, adapter)
    changes = antigravity_workspace_changes(payload, workspace, adapter)
    workspace_install = adapter["workspace_install"]
    workspace_root = workspace / workspace_install["root_name"]
    managed_namespace = workspace_root / workspace_install["payload_target"]
    result: dict[str, Any] = {
        "status": "dry-run" if dry_run else "pending",
        "host": "antigravity",
        "scope": "workspace",
        "target": str(workspace),
        "managed_namespace": str(managed_namespace),
        "changes": changes,
        "backup": None,
        "direct_discovery": {
            "agents": str(workspace_root / workspace_install["agents_target"]),
            "skills": str(workspace_root / workspace_install["skills_target"]),
            "workflows": str(workspace_root / workspace_install["workflows_target"]),
            "rule": str(workspace / workspace_install["instruction_target"]),
        },
    }
    if dry_run:
        return result
    if not assume_yes:
        raise InstallationRefused(
            "Antigravity workspace installation requires explicit confirmation; "
            "rerun with --yes after reviewing --dry-run"
        )

    timestamp = utc_timestamp()
    backup_root = workspace_root / ".antigravity-backups" / timestamp
    stage_root = workspace_root / f".antigravity-workspace-stage-{uuid.uuid4().hex}"
    namespace_source = stage_root / "managed"
    activated: list[tuple[Path, Path | None]] = []
    try:
        ensure_workspace_destination(
            workspace, workspace_root, "Antigravity workspace resource root"
        )
        ensure_workspace_destination(
            workspace, stage_root, "Antigravity workspace staging root"
        )
        ensure_workspace_destination(
            workspace, backup_root, "Antigravity workspace backup root"
        )
        stage_root.mkdir(parents=True, exist_ok=False)
        namespace_source.mkdir(parents=True, exist_ok=True)
        for metadata_name in ("adapter.json", "manifest.json", "profile.json"):
            source = payload / metadata_name
            if source.exists():
                copy_entry(source, namespace_source / metadata_name)

        unchanged = set(changes["unchanged"])
        for source, destination in mapping.items():
            destination = ensure_workspace_destination(
                workspace, destination, "Antigravity workspace target"
            )
            label = destination.relative_to(workspace).as_posix()
            if label in unchanged:
                continue
            if destination.exists():
                _ensure_not_reparse(destination)
            staged = stage_root / "direct" / destination.relative_to(workspace)
            staged.parent.mkdir(parents=True, exist_ok=True)
            copy_entry(source, staged)

        for source, destination in mapping.items():
            destination = ensure_workspace_destination(
                workspace, destination, "Antigravity workspace target"
            )
            label = destination.relative_to(workspace).as_posix()
            if label in unchanged:
                continue
            backup_path: Path | None = None
            if destination.exists():
                backup_path = backup_root / destination.relative_to(workspace)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                _replace_entry(destination, backup_path)
            staged = stage_root / "direct" / destination.relative_to(workspace)
            destination.parent.mkdir(parents=True, exist_ok=True)
            _replace_entry(staged, destination)
            activated.append((destination, backup_path))

        for relative in changes["remove"]:
            destination = workspace_record_target(
                workspace,
                relative,
                antigravity_workspace_record_path(workspace, adapter),
            )
            backup_path = backup_root / Path(relative)
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            _replace_entry(destination, backup_path)
            activated.append((destination, backup_path))

        namespace_backup: Path | None = None
        if managed_namespace.exists():
            _ensure_not_reparse(managed_namespace)
            namespace_backup = backup_root / managed_namespace.relative_to(workspace)
            namespace_backup.parent.mkdir(parents=True, exist_ok=True)
            _replace_entry(managed_namespace, namespace_backup)
        managed_namespace.parent.mkdir(parents=True, exist_ok=True)
        _replace_entry(namespace_source, managed_namespace)
        activated.append((managed_namespace, namespace_backup))

        record = {
            "schema_version": 1,
            "host": "antigravity",
            "scope": "workspace",
            "installed_at": datetime.now(timezone.utc).isoformat(),
            "payload": str(payload),
            "workspace": str(workspace),
            "backup": str(backup_root) if backup_root.exists() else None,
            "direct_targets": sorted(
                destination.relative_to(workspace).as_posix()
                for destination in mapping.values()
            ),
            "direct_digests": {
                destination.relative_to(workspace).as_posix(): entry_digest(destination)
                for destination in mapping.values()
            },
            "removed_targets": list(changes["remove"]),
        }
        write_json_atomic(antigravity_workspace_record_path(workspace, adapter), record)

        required = [
            workspace / workspace_install["instruction_target"],
            workspace_root / workspace_install["router_target"],
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


def resolve_codex_workspace(target: Path) -> Path:
    """Validate an existing project directory for a local Codex installation."""
    raw_workspace = _absolute_without_resolving(target)
    ensure_existing_path_chain_not_reparse(raw_workspace)
    workspace = raw_workspace.resolve()
    home = Path.home().resolve()
    anchor = Path(workspace.anchor).resolve()
    if workspace in {home, anchor}:
        raise InstallationRefused(
            "Refusing a home or filesystem-root workspace; select one project directory"
        )
    if not workspace.is_dir():
        raise InstallationRefused(
            "Codex workspace installation requires an existing project directory"
        )
    if workspace.name.lower() == ".codex":
        raise InstallationRefused(
            "Codex workspace installation requires a project directory, not CODEX_HOME"
        )
    if not workspace.is_relative_to(workspace.anchor):
        raise InstallationRefused("Resolved Codex workspace escaped its filesystem anchor")
    return workspace


def codex_workspace_file_map(payload: Path, workspace: Path) -> dict[Path, Path]:
    """Map the generated payload to project-local Codex policy and resources."""
    mapping: dict[Path, Path] = {}

    def add(source: Path, target: Path) -> None:
        if not source.exists():
            return
        if target in mapping.values():
            raise InstallationRefused(f"Duplicate Codex workspace target: {target}")
        mapping[source] = target

    add(payload / "AGENTS.md", workspace / "AGENTS.md")
    add(payload / "USER_PROFILE.md", workspace / "USER_PROFILE.md")
    content_root = payload / ".agents"
    if not content_root.is_dir():
        raise InstallationRefused("Codex payload is missing its .agents resource tree")

    for source in sorted(content_root.iterdir()):
        if source.is_file():
            add(source, workspace / ".agents" / source.name)
            continue
        for child in sorted(source.iterdir()):
            if source.name == "skills":
                # Codex natively discovers project skills from .codex/skills.
                # Keep the generated .agents tree as a portable V4 reference,
                # but place active skills in Codex's own discovery location.
                add(child, workspace / ".codex" / "skills" / child.name)
            elif source.name == "agents" and child.suffix == ".toml":
                add(child, workspace / ".codex" / "agents" / child.name)
            else:
                add(child, workspace / ".agents" / source.name / child.name)
    return mapping


def codex_workspace_record_path(workspace: Path) -> Path:
    return workspace / ".agents" / "antigravity" / "installation.json"


def codex_workspace_changes(payload: Path, workspace: Path) -> dict[str, list[str]]:
    """Plan a project-local install without replacing unmanaged project files."""
    mapping = codex_workspace_file_map(payload, workspace)
    record_path = codex_workspace_record_path(workspace)
    previous_targets: set[str] = set()
    previous_digests: dict[str, str] = {}
    previous_paths: dict[str, Path] = {}
    if record_path.exists():
        record = load_json(record_path)
        raw_targets = record.get("direct_targets")
        raw_digests = record.get("direct_digests")
        if not isinstance(raw_targets, list) or not all(isinstance(item, str) for item in raw_targets):
            raise InstallationRefused(f"Invalid Codex workspace installation record: {record_path}")
        if not isinstance(raw_digests, dict) or not all(
            isinstance(key, str) and isinstance(value, str) for key, value in raw_digests.items()
        ):
            raise InstallationRefused(f"Invalid Codex workspace ownership record: {record_path}")
        previous_targets = set(raw_targets)
        previous_digests = raw_digests
        previous_paths = {
            label: workspace_record_target(workspace, label, record_path)
            for label in previous_targets | set(previous_digests)
        }

    additions: list[str] = []
    replacements: list[str] = []
    unchanged: list[str] = []
    for source, target in mapping.items():
        target = ensure_workspace_destination(workspace, target, "Codex workspace target")
        label = target.relative_to(workspace).as_posix()
        if not target.exists():
            additions.append(label)
        elif entry_digest(source) == entry_digest(target):
            unchanged.append(label)
        elif label in previous_targets and previous_digests.get(label) == entry_digest(target):
            replacements.append(label)
        else:
            raise InstallationRefused(
                "Refusing to replace unmanaged or locally modified workspace entry: "
                f"{label}. Choose a clean workspace or remove the conflicting entry yourself."
            )

    current_targets = {target.relative_to(workspace).as_posix() for target in mapping.values()}
    stale_targets = sorted(
        label
        for label in previous_targets - current_targets
        if previous_paths[label].exists()
        and previous_digests.get(label) == entry_digest(previous_paths[label])
    )
    return {
        "add": sorted(additions),
        "replace": sorted(replacements),
        "remove": stale_targets,
        "unchanged": sorted(unchanged),
    }


def install_codex_workspace(
    payload: Path,
    target: Path,
    dry_run: bool,
    assume_yes: bool,
) -> dict[str, Any]:
    """Install V4 into one clean Codex project without touching CODEX_HOME."""
    payload = payload.resolve()
    if not payload.is_dir():
        raise InstallationRefused(f"Payload does not exist: {payload}")
    adapter = load_json(payload / "adapter.json")
    if adapter.get("host") != "codex":
        raise InstallationRefused("Codex workspace installation requires a Codex payload")
    workspace = resolve_codex_workspace(target)
    mapping = codex_workspace_file_map(payload, workspace)
    changes = codex_workspace_changes(payload, workspace)
    namespace_target = workspace / ".agents" / "antigravity"
    result: dict[str, Any] = {
        "status": "dry-run" if dry_run else "pending",
        "host": "codex",
        "scope": "workspace",
        "target": str(workspace),
        "namespace": str(namespace_target),
        "changes": changes,
        "backup": None,
    }
    if dry_run:
        return result
    if not assume_yes:
        raise InstallationRefused(
            "Codex workspace installation requires explicit confirmation; rerun with --yes after reviewing --dry-run"
        )

    timestamp = utc_timestamp()
    backup_root = workspace / ".agents" / ".antigravity-backups" / timestamp
    stage_root = workspace / ".agents" / f".antigravity-codex-workspace-stage-{uuid.uuid4().hex}"
    namespace_source = stage_root / "namespace"
    activated: list[tuple[Path, Path | None]] = []
    try:
        ensure_workspace_destination(workspace, stage_root, "Codex workspace staging root")
        ensure_workspace_destination(workspace, backup_root, "Codex workspace backup root")
        ensure_workspace_destination(workspace, namespace_target, "Codex managed namespace")
        stage_root.mkdir(parents=True, exist_ok=False)
        shutil.copytree(payload, namespace_source)
        for source, target_path in mapping.items():
            target_path = ensure_workspace_destination(
                workspace, target_path, "Codex workspace target"
            )
            label = target_path.relative_to(workspace).as_posix()
            if label in changes["unchanged"]:
                continue
            staged = stage_root / "direct" / target_path.relative_to(workspace)
            staged.parent.mkdir(parents=True, exist_ok=True)
            copy_entry(source, staged)

        for source, target_path in mapping.items():
            target_path = ensure_workspace_destination(
                workspace, target_path, "Codex workspace target"
            )
            label = target_path.relative_to(workspace).as_posix()
            if label in changes["unchanged"]:
                continue
            backup_path: Path | None = None
            if target_path.exists():
                _ensure_not_reparse(target_path)
                backup_path = backup_root / target_path.relative_to(workspace)
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                _replace_entry(target_path, backup_path)
            staged = stage_root / "direct" / target_path.relative_to(workspace)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            _replace_entry(staged, target_path)
            activated.append((target_path, backup_path))

        for relative in changes["remove"]:
            target_path = workspace_record_target(
                workspace,
                relative,
                codex_workspace_record_path(workspace),
            )
            backup_path = backup_root / Path(relative)
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            _replace_entry(target_path, backup_path)
            activated.append((target_path, backup_path))

        namespace_backup: Path | None = None
        if namespace_target.exists():
            _ensure_not_reparse(namespace_target)
            namespace_backup = backup_root / ".agents" / "antigravity"
            namespace_backup.parent.mkdir(parents=True, exist_ok=True)
            _replace_entry(namespace_target, namespace_backup)
        namespace_target.parent.mkdir(parents=True, exist_ok=True)
        _replace_entry(namespace_source, namespace_target)
        activated.append((namespace_target, namespace_backup))

        record = {
            "schema_version": 1,
            "host": "codex",
            "scope": "workspace",
            "installed_at": datetime.now(timezone.utc).isoformat(),
            "payload": str(payload),
            "workspace": str(workspace),
            "backup": str(backup_root) if backup_root.exists() else None,
            "direct_targets": sorted(
                target.relative_to(workspace).as_posix() for target in mapping.values()
            ),
            "direct_digests": {
                target.relative_to(workspace).as_posix(): entry_digest(target)
                for target in mapping.values()
            },
            "removed_targets": list(changes["remove"]),
        }
        write_json_atomic(codex_workspace_record_path(workspace), record)
        required = [workspace / "AGENTS.md", workspace / ".agents" / "GLOBAL_MEMORY.md"]
        required.extend(
            workspace / ".codex" / "agents" / source.name
            for source in sorted((payload / ".agents" / "agents").glob("*.toml"))
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
        for target_path, backup_path in reversed(activated):
            if target_path.exists():
                _remove_entry(target_path)
            if backup_path and backup_path.exists():
                backup_path.parent.mkdir(parents=True, exist_ok=True)
                _replace_entry(backup_path, target_path)
        shutil.rmtree(filesystem_path(stage_root), ignore_errors=True)
        raise


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
        (payload / ".agents" / "agents", codex_home / "agents"),
    ):
        if not source_root.exists():
            continue
        for source in sorted(source_root.iterdir()):
            if source_root.name == "agents" and source.suffix != ".toml":
                continue
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
        required = [codex_home / "AGENTS.md", codex_home / "GLOBAL_MEMORY.md"]
        required.extend(
            codex_home / "agents" / source.name
            for source in sorted((payload / ".agents" / "agents").glob("*.toml"))
        )
        missing = [str(path) for path in required if not path.exists()]
        if missing:
            raise InstallationRefused(
                "Post-install validation failed; missing: " + ", ".join(missing)
            )
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
        "--codex-workspace",
        action="store_true",
        help="For host=codex, install into one project workspace plus a rollback namespace",
    )
    install_parser.add_argument(
        "--antigravity-global",
        action="store_true",
        help="For host=antigravity, install into native global discovery locations plus a rollback namespace",
    )
    install_parser.add_argument(
        "--antigravity-workspace",
        action="store_true",
        help="For host=antigravity, install into one project workspace without changing GEMINI_HOME",
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
            if args.codex_workspace and args.host != "codex":
                raise InstallationRefused("--codex-workspace is only valid with --host codex")
            if args.antigravity_global and args.host != "antigravity":
                raise InstallationRefused(
                    "--antigravity-global is only valid with --host antigravity"
                )
            if args.antigravity_workspace and args.host != "antigravity":
                raise InstallationRefused(
                    "--antigravity-workspace is only valid with --host antigravity"
                )
            if sum(
                (
                    args.codex_global,
                    args.codex_workspace,
                    args.antigravity_global,
                    args.antigravity_workspace,
                )
            ) > 1:
                raise InstallationRefused(
                    "Choose only one host-specific installation mode"
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
                        else install_codex_workspace(payload, args.target, True, False)
                        if args.codex_workspace
                        else install_antigravity_global(payload, args.target, True, False)
                        if args.antigravity_global
                        else install_antigravity_workspace(payload, args.target, True, False)
                        if args.antigravity_workspace
                        else install_payload(payload, args.target, args.host, True, False)
                    )
            else:
                payload = build_payload(args.host, selected_profile, selected_packs)
                result = (
                    install_codex_global(payload, args.target, False, args.yes)
                    if args.codex_global
                    else install_codex_workspace(payload, args.target, False, args.yes)
                    if args.codex_workspace
                    else install_antigravity_global(payload, args.target, False, args.yes)
                    if args.antigravity_global
                    else install_antigravity_workspace(payload, args.target, False, args.yes)
                    if args.antigravity_workspace
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
