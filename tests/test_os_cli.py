from __future__ import annotations

import importlib.util
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "global" / "scripts" / "os.py"


def load_os_module():
    spec = importlib.util.spec_from_file_location("antigravity_os_cli", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load Anti-Gravity OS CLI")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class InstallerSafetyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.payload = self.root / "payload"
        self.payload.mkdir()
        (self.payload / "GEMINI.md").write_text("canonical\n", encoding="utf-8")
        (self.payload / "skills").mkdir()
        (self.payload / "skills" / "example.md").write_text("skill\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_dry_run_never_writes(self) -> None:
        target = self.root / "shared-rules"
        target.mkdir()
        sentinel = target / "unrelated-user-rule.md"
        sentinel.write_text("keep me", encoding="utf-8")

        result = self.os_cli.install_payload(
            payload=self.payload,
            target=target,
            host="cursor",
            dry_run=True,
            assume_yes=False,
        )

        self.assertEqual("dry-run", result["status"])
        self.assertTrue(sentinel.exists())
        self.assertFalse((target / "antigravity").exists())

    def test_install_preserves_unrelated_files_and_backs_up_namespace(self) -> None:
        target = self.root / "shared-rules"
        target.mkdir()
        sentinel = target / "unrelated-user-rule.md"
        sentinel.write_text("keep me", encoding="utf-8")
        existing = target / "antigravity"
        existing.mkdir()
        (existing / "GEMINI.md").write_text("old\n", encoding="utf-8")

        result = self.os_cli.install_payload(
            payload=self.payload,
            target=target,
            host="cursor",
            dry_run=False,
            assume_yes=True,
        )

        self.assertEqual("installed", result["status"])
        self.assertEqual("keep me", sentinel.read_text(encoding="utf-8"))
        self.assertEqual(
            "canonical\n",
            (target / "antigravity" / "GEMINI.md").read_text(encoding="utf-8"),
        )
        backup = Path(result["backup"])
        self.assertTrue(backup.exists())
        self.assertEqual("old\n", (backup / "GEMINI.md").read_text(encoding="utf-8"))

    def test_non_dry_run_requires_confirmation(self) -> None:
        target = self.root / "shared-rules"
        target.mkdir()
        with self.assertRaises(self.os_cli.InstallationRefused):
            self.os_cli.install_payload(
                payload=self.payload,
                target=target,
                host="cursor",
                dry_run=False,
                assume_yes=False,
            )

    def test_home_directory_is_refused_as_base_target(self) -> None:
        with self.assertRaises(self.os_cli.InstallationRefused):
            self.os_cli.resolve_install_root(Path.home())

    def test_general_install_option_keeps_optional_packs_dormant(self) -> None:
        profile, packs, option = self.os_cli.resolve_install_option(
            REPO_ROOT,
            "general",
            "general",
            [],
            interactive=False,
        )

        self.assertEqual("general", profile)
        self.assertEqual([], packs)
        self.assertEqual("general", option)

    def test_full_install_option_composes_all_manifest_packs(self) -> None:
        profile, packs, option = self.os_cli.resolve_install_option(
            REPO_ROOT,
            "full",
            "general",
            [],
            interactive=False,
        )

        self.assertEqual("general", profile)
        self.assertEqual(["spatial", "media", "growth"], packs)
        self.assertEqual("full", option)

    def test_install_option_does_not_break_explicit_legacy_selection(self) -> None:
        profile, packs, option = self.os_cli.resolve_install_option(
            REPO_ROOT,
            None,
            "spatial",
            [],
            interactive=False,
        )

        self.assertEqual("spatial", profile)
        self.assertEqual([], packs)
        self.assertEqual("custom", option)

    def test_install_option_rejects_mixed_option_and_pack_flags(self) -> None:
        with self.assertRaises(self.os_cli.InstallationRefused):
            self.os_cli.resolve_install_option(
                REPO_ROOT,
                "full",
                "general",
                ["spatial"],
                interactive=False,
            )


class PayloadActivationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_activation_replaces_payload_without_leaving_a_backup(self) -> None:
        final = self.root / "antigravity" / "general"
        stage = self.root / "antigravity" / ".general-stage"
        final.mkdir(parents=True)
        stage.mkdir(parents=True)
        (final / "version.txt").write_text("old", encoding="utf-8")
        (stage / "version.txt").write_text("new", encoding="utf-8")

        self.os_cli.activate_staged_payload(stage, final)

        self.assertFalse(stage.exists())
        self.assertEqual("new", (final / "version.txt").read_text(encoding="utf-8"))
        self.assertEqual(
            [],
            list((self.root / "antigravity").glob(".general-previous-*")),
        )


class MetadataTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()

    def test_simple_yaml_parser_supports_workflow_lists(self) -> None:
        parsed = self.os_cli.parse_simple_yaml(
            """
id: debug-issue
version: 1
status: active
use_when:
  - A user asks for diagnosis.
  - A failing test needs isolation.
mutation_class: read_only
profiles: [general]
""".strip()
        )
        self.assertEqual("debug-issue", parsed["id"])
        self.assertEqual(1, parsed["version"])
        self.assertEqual(["general"], parsed["profiles"])
        self.assertEqual(2, len(parsed["use_when"]))

    def test_simple_yaml_parser_supports_profile_conditioned_skill_lists(self) -> None:
        parsed = self.os_cli.parse_simple_yaml(
            """
skills: [ui-ux]
conditional_skills:
  - profiles: [spatial]
    skills: [reference-intelligence, storytelling]
  - profiles: [media]
    skills: [video-generation]
""".strip()
        )

        self.assertEqual(["ui-ux"], parsed["skills"])
        self.assertEqual(
            [
                {"profiles": ["spatial"], "skills": ["reference-intelligence", "storytelling"]},
                {"profiles": ["media"], "skills": ["video-generation"]},
            ],
            parsed["conditional_skills"],
        )

    def test_adapter_records_are_valid_json(self) -> None:
        for adapter_path in sorted((REPO_ROOT / "global" / "adapters").glob("*/adapter.json")):
            adapter = json.loads(adapter_path.read_text(encoding="utf-8"))
            self.assertEqual(adapter_path.parent.name, adapter["host"])
            self.assertEqual("antigravity", adapter["namespace"])

        antigravity = json.loads(
            (REPO_ROOT / "global" / "adapters" / "antigravity" / "adapter.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(
            "GEMINI.md",
            antigravity["instruction_target"],
        )

    def test_canonical_repository_passes_validation(self) -> None:
        result = self.os_cli.validate_repository(REPO_ROOT)
        self.assertEqual([], result["issues"])
        self.assertTrue(result["ok"])

    def test_gemini_policy_respects_antigravity_rule_limit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            policy = root / "global" / "GEMINI.md"
            policy.parent.mkdir(parents=True)
            policy.write_text("x" * 12001, encoding="utf-8")

            problems = self.os_cli.validate_markdown(root)

            self.assertTrue(
                any(problem["code"] == "gemini-policy-length" for problem in problems)
            )

    def test_every_host_builds_and_spatial_profile_is_optional(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            for host in self.os_cli.SUPPORTED_HOSTS:
                payload = self.os_cli.build_payload(
                    host=host,
                    profile="general",
                    repo_root=REPO_ROOT,
                    output_root=output,
                )
                adapter = json.loads(
                    (REPO_ROOT / "global" / "adapters" / host / "adapter.json").read_text(
                        encoding="utf-8"
                    )
                )
                self.assertTrue((payload / adapter["instruction_target"]).exists())
                content_root = payload / adapter["content_root"]
                for spatial_skill in (
                    "brand-strategy",
                    "cinematic-motion",
                    "cinematic-showroom-strategy",
                    "master-design-director",
                    "motion-library",
                    "scroll-storyboard",
                    "spatial-experience-design",
                    "storytelling",
                ):
                    self.assertFalse(
                        (content_root / adapter["skills_target"] / spatial_skill).exists()
                    )
                self.assertFalse((content_root / adapter["skills_target"] / "seedance").exists())
                for spatial_workflow in (
                    "workflow-impeccable-animate.md",
                    "workflow-impeccable-craft.md",
                    "workflow-spatial-concept.md",
                    "workflow-spatial-design-ui.md",
                    "workflow-spatial-project-inception.md",
                    "workflow-storytelling.md",
                    "workflow-visual-brainstorm.md",
                ):
                    self.assertFalse(
                        (content_root / adapter["workflows_target"] / spatial_workflow).exists()
                    )

            spatial_payload = self.os_cli.build_payload(
                host="gemini",
                profile="spatial",
                repo_root=REPO_ROOT,
                output_root=output / "spatial",
            )
            self.assertTrue(
                (spatial_payload / "skills" / "spatial-experience-design").exists()
            )
            self.assertTrue((spatial_payload / "skills" / "motion-library").exists())
            self.assertTrue(
                (spatial_payload / "workflows" / "workflow-spatial-project-inception.md").exists()
            )
            self.assertTrue(
                (
                    spatial_payload
                    / "skills"
                    / "spatial-experience-design"
                    / "reference"
                    / "project-phase-routing.md"
                ).is_file()
            )

    def test_spatial_build_uses_windows_safe_sibling_stage_name(self) -> None:
        # A repository-length output root reproduces failures hidden by the much
        # shorter system temporary directory on Windows.
        with tempfile.TemporaryDirectory(prefix=".build-test-", dir=REPO_ROOT) as directory:
            payload = self.os_cli.build_payload(
                host="codex",
                profile="spatial",
                repo_root=REPO_ROOT,
                output_root=Path(directory),
            )
            self.assertTrue(
                payload.joinpath(
                    ".agents", "skills", "cinematic-motion", "SKILL.md"
                ).exists()
            )

    @unittest.skipUnless(os.name == "nt", "Windows-specific long-path behavior")
    def test_spatial_build_copies_deep_references_to_a_long_output_path(self) -> None:
        directory = Path(tempfile.mkdtemp(prefix="antigravity-" + "x" * 88))
        try:
            payload = self.os_cli.build_payload(
                host="antigravity",
                profile="spatial",
                repo_root=REPO_ROOT,
                output_root=directory / "build-output",
            )
            self.assertTrue(
                payload.joinpath(
                    ".agents",
                    "skills",
                    "spatial-experience-design",
                    "reference",
                    "project-phase-routing.md",
                ).is_file()
            )
        finally:
            shutil.rmtree(self.os_cli.filesystem_path(directory), ignore_errors=True)

    def test_antigravity_payload_renders_agents_and_composes_packs(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            general = self.os_cli.build_payload(
                host="antigravity",
                profile="general",
                repo_root=REPO_ROOT,
                output_root=output,
            )
            mixed = self.os_cli.build_payload(
                host="antigravity",
                profile="general",
                packs=("spatial,media",),
                repo_root=REPO_ROOT,
                output_root=output,
            )

            self.assertEqual(output / "antigravity" / "general", general)
            self.assertEqual(output / "antigravity" / "spatial+media", mixed)
            main_policy = (mixed / "GEMINI.md").read_text(encoding="utf-8")
            router = (mixed / ".agents" / "GLOBAL_MEMORY.md").read_text(encoding="utf-8")
            self.assertIn("Main Agent: Studio Director", main_policy)
            self.assertIn("Read `GLOBAL_MEMORY.md` after this policy", main_policy)
            self.assertIn("The **Studio Director** is the main agent", router)
            self.assertIn("`design-director`", router)
            generated_agents = sorted(
                path.relative_to(general / ".agents" / "agents").as_posix()
                for path in (general / ".agents" / "agents").rglob("agent.md")
            )
            self.assertEqual(
                [
                    "assurance-quality-lead/agent.md",
                    "design-director/agent.md",
                    "product-strategy-lead/agent.md",
                    "staff-engineer/agent.md",
                    "studio-director/agent.md",
                    "systems-architect/agent.md",
                ],
                generated_agents,
            )
            assurance = (
                general / ".agents" / "agents" / "assurance-quality-lead" / "agent.md"
            ).read_text(encoding="utf-8")
            self.assertIn("mainAgent: true", assurance)
            self.assertIn("subagent: true", assurance)
            self.assertIn("  - list_dir", assurance)
            self.assertNotIn("replace_file_content", assurance)
            self.assertIn("GLOBAL_MEMORY.md", assurance)
            general_design = (
                general / ".agents" / "agents" / "design-director" / "agent.md"
            ).read_text(encoding="utf-8")
            mixed_design = (
                mixed / ".agents" / "agents" / "design-director" / "agent.md"
            ).read_text(encoding="utf-8")
            self.assertNotIn("\nskills:\n", general_design)
            self.assertIn("`reference-intelligence`", general_design)
            self.assertIn("## Available capability routes", mixed_design)
            self.assertIn("`canvas-ui`", mixed_design)
            self.assertIn("`video-generation`", mixed_design)
            self.assertNotIn("\nskills:\n", mixed_design)
            self.assertIn("surface `video-generation`", mixed_design)
            self.assertIn("select `reference-intelligence` without requiring Beloved", mixed_design)
            self.assertIn("optional Gemini multimodal plugin", mixed_design)
            mixed_director = (
                mixed / ".agents" / "agents" / "studio-director" / "agent.md"
            ).read_text(encoding="utf-8")
            self.assertIn("the evidence to the Design Director and `reference-intelligence`", mixed_director)
            self.assertIn("before any of\nthose effects", mixed_director)
            self.assertFalse((general / ".agents" / "skills" / "seedance").exists())
            self.assertFalse((general / ".agents" / "reference" / "interior-archetypes.md").exists())
            self.assertTrue((mixed / ".agents" / "skills" / "video-generation").exists())
            self.assertFalse((mixed / ".agents" / "skills" / "seedance").exists())
            self.assertTrue((mixed / ".agents" / "reference" / "interior-archetypes.md").exists())

    def test_growth_pack_is_opt_in_and_general_is_implicit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            general = self.os_cli.build_payload(
                host="codex",
                profile="general",
                repo_root=REPO_ROOT,
                output_root=output,
            )
            growth = self.os_cli.build_payload(
                host="codex",
                profile="general",
                packs=("growth",),
                repo_root=REPO_ROOT,
                output_root=output,
            )
            self.assertFalse((general / ".agents" / "skills" / "copywriting").exists())
            self.assertTrue(
                (general / ".agents" / "reference" / "customer-market-demand-evidence.md").exists()
            )
            self.assertTrue(
                (general / ".agents" / "reference" / "meaning-and-evidence-foundation.md").exists()
            )
            self.assertTrue((growth / ".agents" / "skills" / "copywriting").exists())
            self.assertTrue((growth / ".agents" / "skills" / "coding").exists())
            general_product = (
                general / ".agents" / "agents" / "product-strategy-lead" / "agent.md"
            ).read_text(encoding="utf-8")
            growth_product = (
                growth / ".agents" / "agents" / "product-strategy-lead" / "agent.md"
            ).read_text(encoding="utf-8")
            self.assertNotIn("skills/copywriting", general_product)
            self.assertIn("skills/copywriting", growth_product)
            self.assertFalse((general / ".agents" / "skills" / "offer-architecture").exists())
            self.assertTrue((growth / ".agents" / "skills" / "offer-architecture").exists())
            self.assertFalse(
                (general / ".agents" / "workflows" / "workflow-commercial-decision-record.md").exists()
            )
            self.assertTrue(
                (growth / ".agents" / "workflows" / "workflow-commercial-decision-record.md").exists()
            )
            self.assertTrue(
                (growth / ".agents" / "workflows" / "workflow-live-learning-loop.md").exists()
            )
            self.assertTrue(
                (growth / ".agents" / "reference" / "growth-direct-selection.md").exists()
            )
            with self.assertRaises(self.os_cli.AntiGravityError):
                self.os_cli.resolve_pack_selection(
                    json.loads((REPO_ROOT / "global" / "manifest.yaml").read_text(encoding="utf-8")),
                    "general",
                    ("general",),
                )


class WorkflowStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()

    def state(self, task_id: str) -> dict:
        return {
            "schema_version": 1,
            "task_id": task_id,
            "workflow_id": "build-feature",
            "mode": "implement",
            "status": "in_progress",
            "current_state": "execute-if-authorized",
            "completed_states": ["intake", "assess"],
            "owner": {"agent": task_id, "thread": task_id, "worktree": None},
            "workspace": "temporary",
            "lease": None,
            "evidence": [],
            "artifacts": [],
            "approvals": [],
            "blockers": [],
            "next_action": "Continue implementation.",
            "created_at": "2026-07-13T00:00:00Z",
            "updated_at": "2026-07-13T00:00:00Z",
            "archived": False,
        }

    def test_independent_tasks_receive_distinct_state_and_index_entries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            first = self.os_cli.write_workflow_state(workspace, self.state("task-one"))
            second = self.os_cli.write_workflow_state(workspace, self.state("task-two"))

            self.assertNotEqual(first, second)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            index = json.loads(
                (workspace / ".agents" / "workflows" / "index.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertEqual("task-one.json", index["tasks"]["task-one"])
            self.assertEqual("task-two.json", index["tasks"]["task-two"])

    def test_invalid_task_id_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                self.os_cli.write_workflow_state(
                    Path(directory), self.state("../escaped-task")
                )


class CoreRouteContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()

    def workflow_metadata(self, workflow_id: str) -> tuple[dict, str]:
        path = REPO_ROOT / "global" / "workflows" / f"workflow-{workflow_id}.md"
        text = path.read_text(encoding="utf-8")
        _, frontmatter, body = text.split("---", 2)
        return self.os_cli.parse_simple_yaml(frontmatter), body

    def skill_metadata(self, skill_id: str) -> tuple[dict, str]:
        path = REPO_ROOT / "global" / "skills" / skill_id / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        _, frontmatter, body = text.split("---", 2)
        return self.os_cli.parse_simple_yaml(frontmatter), body

    def test_project_inception_is_proposal_first_and_proportionate(self) -> None:
        metadata, body = self.workflow_metadata("project-inception")

        self.assertEqual(3, metadata["version"])
        self.assertEqual("read_only", metadata["mutation_class"])
        self.assertIn("plan-architecture", metadata["next_workflows"])
        self.assertIn("decision-ready first-direction workflow", body)
        self.assertIn("Force every request through research", body)
        self.assertIn("Invent project facts", body)
        self.assertIn("Path A may collapse to a task statement", body)
        self.assertIn("Use `task-dispatch` only when a bounded worker", body)
        self.assertIn("before writing project contexts", metadata["approval_gates"][0])

    def test_task_dispatch_requires_a_real_delegation_case(self) -> None:
        metadata, body = self.workflow_metadata("task-dispatch")
        director = (
            REPO_ROOT / "global" / "agents" / "studio-director" / "AGENT.md"
        ).read_text(encoding="utf-8")

        self.assertEqual(2, metadata["version"])
        self.assertEqual("read_only", metadata["mutation_class"])
        self.assertIn("exclusive ownership", metadata["use_when"][0])
        self.assertIn("If any answer is no, do not dispatch", body)
        self.assertIn("Never create workers to simulate activity", body)
        self.assertIn("Read the changed files or decision artifact", body)
        self.assertIn("Delegate only when every answer is yes", director)
        self.assertIn("Never create a swarm to look busy", director)
        self.assertIn("inspect the artifact or changed files", director)

    def test_debug_issue_keeps_diagnosis_read_only_until_an_authorized_repair(self) -> None:
        metadata, body = self.workflow_metadata("debug-issue")

        self.assertEqual(2, metadata["version"])
        self.assertEqual("local_edit", metadata["mutation_class"])
        self.assertIn("incident-response", metadata["next_workflows"])
        self.assertIn(".agents/workflows/<task-id>.json", metadata["resume_contract"])
        self.assertIn("diagnose and propose remain read-only", metadata["approval_gates"][0])
        self.assertIn("A mitigation is not described as root-cause confirmation", body)
        self.assertIn("Do not delete/skip tests", body)
        self.assertNotIn("debug-issue.json using", metadata["resume_contract"])

    def test_rebuilt_high_consequence_routes_keep_current_authority_boundaries(self) -> None:
        expected_classes = {
            "build-feature": "local_edit",
            "plan-architecture": "read_only",
            "security-audit": "read_only",
            "ship-to-production": "external_or_production",
            "database-migration": "external_or_production",
            "dependency-upgrade": "dependency_or_network",
            "incident-response": "external_or_production",
        }
        required_body_rules = {
            "build-feature": "The selected roles may loop",
            "plan-architecture": "Do not manufacture three tiers",
            "security-audit": "Never say “secure,” “compliant,” or “safe for production”",
            "ship-to-production": "Readiness is not approval",
            "database-migration": "No database or data mutation is permitted",
            "dependency-upgrade": "The safe default is a read-only recommendation",
            "incident-response": "Keep mitigation and root cause separate",
        }

        for workflow_id, mutation_class in expected_classes.items():
            metadata, body = self.workflow_metadata(workflow_id)
            self.assertEqual(2, metadata["version"])
            self.assertEqual(mutation_class, metadata["mutation_class"])
            self.assertIn(".agents/workflows/<task-id>.json", metadata["resume_contract"])
            self.assertIn(required_body_rules[workflow_id], body)
            self.assertNotIn("skill-", body)

        for workflow_id in (
            "ship-to-production",
            "database-migration",
            "dependency-upgrade",
            "incident-response",
        ):
            metadata, _ = self.workflow_metadata(workflow_id)
            self.assertTrue(
                any("just-in-time approval" in gate for gate in metadata["approval_gates"])
            )

    def test_test_strategy_selects_evidence_without_claiming_a_release(self) -> None:
        metadata, body = self.workflow_metadata("test-strategy")

        self.assertEqual(2, metadata["version"])
        self.assertEqual("local_edit", metadata["mutation_class"])
        self.assertIn("verify-project", metadata["next_workflows"])
        self.assertIn("propose and review remain read-only", metadata["approval_gates"][0])
        self.assertIn("Select the smallest credible evidence", body)
        self.assertIn("Neither this workflow nor a passing test suite authorizes a release", body)
        self.assertIn("retry success is not diagnosis", body)

    def test_verify_project_interprets_evidence_without_deployment_authority(self) -> None:
        metadata, body = self.workflow_metadata("verify-project")

        self.assertEqual(2, metadata["version"])
        self.assertEqual("read_only", metadata["mutation_class"])
        self.assertIn("ship-to-production", metadata["next_workflows"])
        self.assertIn(".agents/workflows/<task-id>.json", metadata["resume_contract"])
        self.assertIn("This is a read-only evidence-gathering", body)
        self.assertIn("verified with residual risk", body)
        self.assertIn("It cannot substitute for missing tests or authorize deployment", body)

    def test_growth_commercial_routes_preserve_direct_work_and_external_gates(self) -> None:
        decision_metadata, decision_body = self.workflow_metadata("commercial-decision-record")
        learning_metadata, learning_body = self.workflow_metadata("live-learning-loop")
        direct_selection = (
            REPO_ROOT / "global" / "reference" / "growth-direct-selection.md"
        ).read_text(encoding="utf-8")

        self.assertEqual(1, decision_metadata["version"])
        self.assertEqual(["growth"], decision_metadata["profiles"])
        self.assertEqual("local_edit", decision_metadata["mutation_class"])
        self.assertIn(".agents/workflows/<task-id>.json", decision_metadata["resume_contract"])
        self.assertIn("not a proposal generator", decision_body)
        self.assertIn("does not send, publish, negotiate, price, collect", decision_body)
        self.assertEqual(1, learning_metadata["version"])
        self.assertEqual(["growth"], learning_metadata["profiles"])
        self.assertEqual("external_or_production", learning_metadata["mutation_class"])
        self.assertIn("just-in-time approval", learning_body)
        self.assertIn("never call it causal proof", learning_body)
        self.assertIn("do not turn a direct task into a workflow", direct_selection)
        self.assertIn("contact always needs separate approval", direct_selection)

    def test_video_generation_is_an_optional_media_only_direct_skill_route(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / "global" / "manifest.yaml").read_text(encoding="utf-8")
        )
        workflow_ids = {workflow["id"] for workflow in manifest["workflows"]}
        fixture = json.loads(
            (REPO_ROOT / "tests" / "fixtures" / "routing.json").read_text(encoding="utf-8")
        )
        route = next(scenario for scenario in fixture["scenarios"] if scenario["id"] == "media-direction")
        metadata, body = self.skill_metadata("video-generation")

        self.assertNotIn("video-generation", workflow_ids)
        self.assertFalse(
            (REPO_ROOT / "global" / "workflows" / "workflow-video-generation.md").exists()
        )
        self.assertEqual(3, fixture["schema_version"])
        self.assertEqual("skill", route["route_kind"])
        self.assertEqual("video-generation", route["route"])
        self.assertEqual("video-generation", metadata["name"])
        self.assertIn("Google Flow", body)

    def test_named_general_ui_operations_are_direct_skill_routes_not_workflows(self) -> None:
        retired_operations = {
            "adapt", "audit", "bolder", "clarify", "colorize", "critique",
            "delight", "distill", "document", "extract", "harden", "layout",
            "live", "onboard", "optimize", "overdrive", "polish", "quieter",
            "shape", "teach", "typeset",
        }
        manifest = json.loads(
            (REPO_ROOT / "global" / "manifest.yaml").read_text(encoding="utf-8")
        )
        registered_ids = {workflow["id"] for workflow in manifest["workflows"]}

        self.assertFalse(
            {f"impeccable-{operation}" for operation in retired_operations}
            & registered_ids
        )
        for operation in retired_operations:
            self.assertFalse(
                (REPO_ROOT / "global" / "workflows" / f"workflow-impeccable-{operation}.md").exists()
            )

        design_metadata, design_body = self.workflow_metadata("design-ui")
        ui_ux = (REPO_ROOT / "global" / "skills" / "ui-ux" / "SKILL.md").read_text(encoding="utf-8")
        operation_routing = (
            REPO_ROOT / "global" / "skills" / "ui-ux" / "reference" / "operation-routing.md"
        ).read_text(encoding="utf-8")
        build_feature = (
            REPO_ROOT / "global" / "workflows" / "workflow-build-feature.md"
        ).read_text(encoding="utf-8")

        self.assertEqual(2, design_metadata["version"])
        self.assertIn("proportionate general-interface design effort", design_metadata["intent"])
        self.assertNotIn("Impeccable", design_body)
        self.assertIn("Treat it as a direct task mode, not a workflow", ui_ux)
        self.assertIn("never trigger an automatic chain of work", operation_routing)
        self.assertIn("Use this reference only for a direct named UI operation", (
            REPO_ROOT / "global" / "skills" / "ui-ux" / "reference" / "interface-operation-playbook.md"
        ).read_text(encoding="utf-8"))
        self.assertNotIn("Impeccable Design Authority", build_feature)

    def test_ui_craft_and_product_motion_methods_are_direct_and_discoverable(self) -> None:
        ui_ux_root = REPO_ROOT / "global" / "skills" / "ui-ux"
        ui_ux = (ui_ux_root / "SKILL.md").read_text(encoding="utf-8")
        resource_index = (ui_ux_root / "references" / "resource-index.md").read_text(
            encoding="utf-8"
        )
        implementation = (
            ui_ux_root / "reference" / "ui-implementation-handoff.md"
        ).read_text(encoding="utf-8")
        product_motion = (
            ui_ux_root / "reference" / "product-motion-contract.md"
        ).read_text(encoding="utf-8")

        self.assertFalse(
            (REPO_ROOT / "global" / "workflows" / "workflow-ui-craft.md").exists()
        )
        self.assertFalse(
            (REPO_ROOT / "global" / "workflows" / "workflow-ui-animate.md").exists()
        )
        self.assertIn("ui-implementation-handoff.md", ui_ux)
        self.assertIn("product-motion-contract.md", ui_ux)
        self.assertIn("ui-implementation-handoff.md", resource_index)
        self.assertIn("product-motion-contract.md", resource_index)
        self.assertIn("data and failure boundary", implementation)
        self.assertIn("project-native checks", implementation)
        self.assertIn("Changed artefacts", implementation)
        self.assertIn("purpose -> trigger -> affected state/property", product_motion)
        self.assertIn("interruption behaviour", product_motion)
        self.assertIn("existing project motion primitives", product_motion)
        self.assertIn("pointer, keyboard, and touch", product_motion)
        self.assertIn("`cinematic-motion`", product_motion)

    def test_low_risk_general_operations_are_direct_skill_routes_not_workflows(self) -> None:
        retired_routes = {
            "design-api": "api-design",
            "optimize-performance": "performance",
            "refactor-module": "refactoring",
            "review-code": "review-audit",
            "ui-craft": "ui-ux",
            "ui-animate": "ui-ux",
        }
        manifest = json.loads(
            (REPO_ROOT / "global" / "manifest.yaml").read_text(encoding="utf-8")
        )
        registered_ids = {workflow["id"] for workflow in manifest["workflows"]}

        for route, owner in retired_routes.items():
            self.assertNotIn(route, registered_ids)
            self.assertFalse(
                (REPO_ROOT / "global" / "workflows" / f"workflow-{route}.md").exists()
            )
            self.assertTrue(
                (REPO_ROOT / "global" / "skills" / owner / "SKILL.md").is_file()
            )

        router = (REPO_ROOT / "global" / "GLOBAL_MEMORY.md").read_text(encoding="utf-8")
        ui_ux = (REPO_ROOT / "global" / "skills" / "ui-ux" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("use `api-design` directly", router)
        self.assertIn("direct `review-audit`", router)
        self.assertIn("Add motion without purpose", ui_ux)

    def test_context_hygiene_is_authority_safe_direct_support_not_a_workflow(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / "global" / "manifest.yaml").read_text(encoding="utf-8")
        )
        workflow_ids = {workflow["id"] for workflow in manifest["workflows"]}
        skill = (REPO_ROOT / "global" / "skills" / "context-hygiene" / "SKILL.md").read_text(
            encoding="utf-8"
        )

        self.assertNotIn("context-hygiene", workflow_ids)
        self.assertFalse(
            (REPO_ROOT / "global" / "workflows" / "workflow-context-hygiene.md").exists()
        )
        self.assertIn("only when authorised", skill)
        self.assertIn("Never overwrite another task's state record", skill)
        self.assertIn("## OUTPUT SHAPE", skill)

    def test_studio_router_keeps_packs_optional_and_motion_library_bounded(self) -> None:
        router = (REPO_ROOT / "global" / "GLOBAL_MEMORY.md").read_text(encoding="utf-8")

        self.assertIn("Use this as a router, not a giant prompt", router)
        self.assertIn("A pack changes discoverability only; it never changes authority", router)
        self.assertIn("motion-library` is a Spatial reference selector", router)
        self.assertIn("No route is mandatory for a small reversible task", router)
        self.assertNotIn("Impeccable is the design authority", router)

    def test_product_framing_delays_technical_routes_until_a_named_decision(self) -> None:
        router = (REPO_ROOT / "global" / "GLOBAL_MEMORY.md").read_text(encoding="utf-8")
        policy = (REPO_ROOT / "global" / "GEMINI.md").read_text(encoding="utf-8")
        director = (
            REPO_ROOT / "global" / "agents" / "studio-director" / "AGENT.md"
        ).read_text(encoding="utf-8")
        product = (
            REPO_ROOT / "global" / "agents" / "product-strategy-lead" / "AGENT.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Technical loading gate for product framing", router)
        self.assertIn("Do not select `coding`, `testing`,", router)
        self.assertIn("Studio Director directly for a small framing task", router)
        self.assertIn("available", router)
        self.assertIn("selected", router)
        self.assertIn("loaded", router)
        self.assertIn("used", router)
        self.assertIn("For product framing, keep the first pass decision-focused", policy)
        self.assertIn("Do not load `coding`, `testing`,", policy)
        self.assertIn("do not select implementation, API, database,", director)
        self.assertIn("do not prescribe endpoints, schemas, libraries, or", product)
        self.assertIn("Record stack, identity, persistence", product)
        product_skill = (REPO_ROOT / "global" / "skills" / "product-thinking" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Calibrate confidence to evidence", product_skill)
        self.assertIn("Resolve product unknowns before technical commitment", product_skill)
        self.assertIn("generic conventions do not", router)
        self.assertIn("high-confidence project conclusion", router)
        director_path = REPO_ROOT / "global" / "agents" / "studio-director" / "AGENT.md"
        director_metadata, _ = self.os_cli.split_frontmatter(director_path)
        self.assertEqual(
            ["deep-think", "context-hygiene", "product-thinking", "to-tickets"],
            director_metadata["skills"],
        )

    def test_customer_market_evidence_reference_is_conditional_and_non_authorising(self) -> None:
        reference = (
            REPO_ROOT / "global" / "reference" / "customer-market-demand-evidence.md"
        ).read_text(encoding="utf-8")
        router = (REPO_ROOT / "global" / "GLOBAL_MEMORY.md").read_text(encoding="utf-8")

        self.assertIn("conditional shared reference", reference)
        self.assertIn("does **not** create a compulsory discovery phase", reference)
        self.assertIn("Read-only public desk research", reference)
        self.assertIn("Stop for explicit human approval before", reference)
        self.assertIn("A low-risk copy improvement remains direct work", reference)
        self.assertIn("never authorises external research or external effects", router)

    def test_meaning_and_evidence_foundation_is_conditional_and_preserves_owners(self) -> None:
        reference = (
            REPO_ROOT / "global" / "reference" / "meaning-and-evidence-foundation.md"
        ).read_text(encoding="utf-8")
        router = (REPO_ROOT / "global" / "GLOBAL_MEMORY.md").read_text(encoding="utf-8")

        self.assertIn("conditional shared reference", reference)
        self.assertIn("does **not** activate the Growth or Spatial pack", reference)
        self.assertIn("A clear local correction, grammar fix, or bounded rewrite remains direct work", reference)
        self.assertIn("Never invent customer language, testimonials, credentials, results", reference)
        self.assertIn("Stop for explicit human approval immediately before an external effect", reference)
        self.assertIn("Spatial taste, materiality, and premium direction remain specialist", reference)
        self.assertIn("not a baseline and not a sixth permanent Growth capability", router)


class CoreSkillContractTests(unittest.TestCase):
    def skill_text(self, skill_id: str) -> str:
        return (
            REPO_ROOT / "global" / "skills" / skill_id / "SKILL.md"
        ).read_text(encoding="utf-8")

    def skill_description(self, skill_id: str) -> str:
        text = self.skill_text(skill_id)
        _, frontmatter, _ = text.split("---", 2)
        return frontmatter

    def test_core_skill_descriptions_name_neighbouring_exclusions(self) -> None:
        for skill_id in ("product-thinking", "architecture", "debugging", "testing"):
            self.assertIn("Do NOT use", self.skill_description(skill_id))

    def test_copy_skills_preserve_distinct_jobs_and_proof_boundaries(self) -> None:
        copywriting = self.skill_text("copywriting")
        copy_editing = self.skill_text("copy-editing")

        self.assertIn("Never invent customer language, testimonials, credentials, results", copywriting)
        self.assertIn("Learn more\" can be appropriate", copywriting)
        self.assertIn("meaning-and-evidence-foundation.md", copywriting)
        self.assertNotIn(".claude/", copywriting)
        self.assertNotIn("contexts/story.md", copywriting)

        self.assertIn("Never silently change the original audience, offer", copy_editing)
        self.assertIn("Never run all seven sweeps", copy_editing)
        self.assertIn("Never make copy more specific than the available evidence", copy_editing)
        self.assertIn("meaning-and-evidence-foundation.md", copy_editing)
        self.assertNotIn(".claude/", copy_editing)

    def test_expert_positioning_keeps_posture_as_a_contextual_commercial_choice(self) -> None:
        positioning = self.skill_text("expert-positioning")
        posture_reference = (
            REPO_ROOT
            / "global"
            / "skills"
            / "expert-positioning"
            / "references"
            / "professional-services-posture.md"
        ).read_text(encoding="utf-8")

        self.assertIn("as a universal sales policy", positioning)
        self.assertIn("Select the commercial posture with the user", positioning)
        self.assertIn("I’d love to help\" is not automatically a defect", positioning)
        self.assertIn("meaning-and-evidence-foundation.md", positioning)
        self.assertIn("Do not assume every strategy fragment must be paid", posture_reference)
        self.assertIn("Do not rename an ordinary sales call as a paid diagnostic", posture_reference)

    def test_marketing_psychology_is_an_ethics_bounded_hypothesis_route(self) -> None:
        psychology = self.skill_text("marketing-psychology")
        catalogue = (
            REPO_ROOT
            / "global"
            / "skills"
            / "marketing-psychology"
            / "references"
            / "extended-guidance.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Never recommend fake scarcity", psychology)
        self.assertIn("Start with the person’s decision", psychology)
        self.assertIn("Do not claim improved conversion or causal impact", psychology)
        self.assertIn("evidence review in progress", catalogue)
        self.assertIn("**not** a tactics manual", catalogue)

    def test_media_safety_is_owned_by_the_single_video_generation_package(self) -> None:
        video_root = REPO_ROOT / "global" / "skills" / "video-generation"
        skill = (video_root / "SKILL.md").read_text(encoding="utf-8")
        diagnosis = (video_root / "references" / "evaluation-and-diagnosis.md").read_text(encoding="utf-8")
        rights = (video_root / "references" / "rights-provenance-and-confidentiality.md").read_text(encoding="utf-8")
        handoff = (video_root / "references" / "production-handoff-and-automation.md").read_text(encoding="utf-8")
        brief = (video_root / "references" / "brief-and-prompt-composition.md").read_text(encoding="utf-8")

        self.assertIn("Never use a provider's tags", skill)
        self.assertIn("Never translate, disguise, retry", diagnosis)
        self.assertIn("Never remove, hide, or advise circumventing", rights)
        self.assertIn("Keep credentials", handoff)
        self.assertNotIn("<API_KEY>", handoff)
        self.assertIn("Fixed prompt length", brief)
        self.assertFalse((REPO_ROOT / "global" / "skills" / "seedance").exists())

    def test_debugging_preserves_evidence_and_authority_over_rigid_patch_rules(self) -> None:
        debugging = self.skill_text("debugging")
        resource_root = REPO_ROOT / "global" / "skills" / "debugging"

        self.assertIn("not a universal gate", debugging)
        self.assertIn("No justified code change", debugging)
        self.assertIn("incident-mitigate", debugging)
        self.assertIn("unverified` theory cannot authorize a repair", debugging)
        self.assertNotIn("Attempt a 4th fix", debugging)
        self.assertNotIn("MUST construct a deterministic test", debugging)
        for relative_path in (
            "references/evidence-and-hypotheses.md",
            "references/fault-class-map.md",
            "references/incident-and-repair-boundaries.md",
            "references/resource-index.md",
            "evals/debugging-scenarios.md",
        ):
            self.assertTrue((resource_root / relative_path).is_file())

    def test_product_thinking_uses_proportionate_evidence(self) -> None:
        product = self.skill_text("product-thinking")

        self.assertIn("decision-quality reflex, not a mandatory discovery phase", product)
        self.assertIn("Match evidence to the claim", product)
        self.assertIn("Instrument only when", product)
        self.assertIn("Compare the simplest non-AI", product)
        self.assertIn("Turn a clear, reversible, low-consequence change", product)

    def test_architecture_uses_decision_sized_options(self) -> None:
        architecture = self.skill_text("architecture")

        self.assertIn("Compare only viable options", architecture)
        self.assertIn("when the architecture actually has replicated", architecture)
        self.assertNotIn("Present three tiers", architecture)

    def test_colour_method_is_a_conditional_uiux_reference_not_a_second_skill(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / "global" / "manifest.yaml").read_text(encoding="utf-8")
        )
        active_skill_ids = {entry["id"] for entry in manifest["skills"]}
        ui_ux = self.skill_text("ui-ux")
        method = (
            REPO_ROOT
            / "global"
            / "skills"
            / "ui-ux"
            / "reference"
            / "color-and-contrast.md"
        ).read_text(encoding="utf-8")
        evidence = (
            REPO_ROOT
            / "global"
            / "skills"
            / "ui-ux"
            / "reference"
            / "color-evidence-and-context.md"
        ).read_text(encoding="utf-8")

        self.assertNotIn("color-system", active_skill_ids)
        self.assertFalse((REPO_ROOT / "global" / "skills" / "color-system").exists())
        self.assertTrue(
            (REPO_ROOT / "global" / "archives" / "color-system-v3-source" / "SKILL.md").is_file()
        )
        self.assertIn("color-and-contrast.md", ui_ux)
        self.assertIn("color-evidence-and-context.md", ui_ux)
        self.assertIn("Do not use colour as the only cue", method)
        self.assertIn("4.5:1", method)
        self.assertIn("context-dependent hypotheses", method)
        self.assertIn("Never infer a person's or market's colour preference", evidence)
        self.assertIn("A valid experiment", evidence)

    def test_testing_has_portable_routes_and_a_risk_sized_output(self) -> None:
        testing = self.skill_text("testing")
        resource_root = REPO_ROOT / "global" / "skills" / "testing"

        self.assertNotIn("skill-coding.md", testing)
        self.assertNotIn("100x–1000x", testing)
        self.assertIn("Testing is evidence selection under risk", testing)
        self.assertIn("a single green command", testing)
        self.assertIn("verified with residual risk", testing)
        self.assertIn("a scanner", testing)
        self.assertNotIn("developer confidence to deploy rapidly", testing)
        for relative_path in (
            "references/evidence-selection.md",
            "references/oracles-and-stability.md",
            "references/ai-feature-evaluation.md",
            "references/release-evidence.md",
            "references/resource-index.md",
            "evals/testing-scenarios.md",
        ):
            self.assertTrue((resource_root / relative_path).is_file())

    def test_prospect_research_prepares_external_actions_without_executing_them(self) -> None:
        prospect_research = self.skill_text("prospect-research")
        resource_root = REPO_ROOT / "global" / "skills" / "prospect-research"

        self.assertIn("AUTHORITY AND EXTERNAL-ACTION BOUNDARY", prospect_research)
        self.assertIn("does not contact a prospect", prospect_research)
        self.assertIn("without approval", prospect_research)
        self.assertNotIn("Send high-personalization outreach", prospect_research)
        self.assertTrue((resource_root / "references" / "prospect-dossier-template.md").is_file())
        self.assertTrue((resource_root / "scripts" / "dossier_helper.py").is_file())


if __name__ == "__main__":
    unittest.main()
