from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
GLOBAL = REPO_ROOT / "global"
MODULE_PATH = GLOBAL / "scripts" / "os.py"

CORE_ARTIFACTS = (
    "evidence-dossier.md",
    "creative-brief.md",
    "concept-directions.md",
    "experience-blueprint.md",
    "production-plan.md",
)

AFFECTED_SKILLS = (
    "brand-strategy",
    "storytelling",
    "spatial-experience-design",
    "cinematic-motion",
    "scroll-storyboard",
    "master-design-director",
    "motion-library",
    "cinematic-showroom-strategy",
    "media-choreography",
    "spatial-outreach-site-sprint",
)

HIGH_STAKES_WORKFLOWS = ("workflow-spatial-project-inception.md",)

RETIRED_SPATIAL_ROUTE_FILES = (
    "workflow-reference-intelligence.md",
    "workflow-visual-brainstorm.md",
    "workflow-spatial-concept.md",
    "workflow-storytelling.md",
    "workflow-spatial-design-ui.md",
    "workflow-impeccable-craft.md",
    "workflow-impeccable-animate.md",
)


def load_os_module():
    spec = importlib.util.spec_from_file_location("antigravity_os_cli_spatial", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load Anti-Gravity OS CLI")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class SpatialWorkflowContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()
        self.manifest = json.loads(read(GLOBAL / "manifest.yaml"))

    def test_five_core_templates_are_registered_only_for_spatial_profile(self) -> None:
        records = {record["id"]: record for record in self.manifest["context_templates"]}
        for filename in CORE_ARTIFACTS:
            identifier = filename.removesuffix(".md")
            self.assertIn(identifier, records)
            self.assertEqual(["spatial"], records[identifier]["profiles"])
            self.assertTrue((GLOBAL / "context_templates" / filename).exists())

    def test_general_payload_has_no_spatial_workflow_or_contract_templates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            payload = self.os_cli.build_payload(
                host="codex",
                profile="general",
                repo_root=REPO_ROOT,
                output_root=Path(directory),
            )
            root = payload / ".agents"
            self.assertFalse((root / "workflows" / "workflow-spatial-project-inception.md").exists())
            for filename in CORE_ARTIFACTS:
                self.assertFalse((root / "context_templates" / filename).exists())


    def test_spatial_workflow_uses_v5_constitution_and_risk_first_prototype(self) -> None:
        inception = read(GLOBAL / "workflows" / HIGH_STAKES_WORKFLOWS[0])
        self.assertIn("v5-creative-constitution-v1.0.0.md", inception)
        self.assertIn("Study", inception)
        self.assertIn("Explore", inception)
        self.assertIn("Provisional", inception)
        self.assertIn("Committed", inception)
        self.assertIn("test the risk that could change the decision", inception.lower())
        self.assertIn("not stages that must be completed in order", inception)

    def test_motion_library_is_spatial_only_and_profile_resources_close(self) -> None:
        skill = next(record for record in self.manifest["skills"] if record["id"] == "motion-library")
        self.assertEqual(["spatial"], skill["profiles"])

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            general = self.os_cli.build_payload(
                host="codex",
                profile="general",
                repo_root=REPO_ROOT,
                output_root=output / "general",
            )
            spatial = self.os_cli.build_payload(
                host="codex",
                profile="spatial",
                repo_root=REPO_ROOT,
                output_root=output / "spatial",
            )
            general_library = general / ".agents" / "skills" / "motion-library"
            spatial_library = spatial / ".agents" / "skills" / "motion-library"
            spatial_motion = spatial / ".agents" / "skills" / "cinematic-motion"

            self.assertFalse(general_library.exists())
            self.assertTrue(spatial_library.exists())
            self.assertTrue((spatial_motion / "reference").is_dir())
            self.assertTrue((spatial_motion / "references" / "resource-index.md").is_file())

    def test_general_manifest_routing_has_no_spatial_only_dependency(self) -> None:
        profiles = {record["id"]: set(record["profiles"]) for record in self.manifest["workflows"]}
        for record in self.manifest["workflows"]:
            if "general" not in record["profiles"]:
                continue
            workflow_path = REPO_ROOT / record["path"]
            metadata, _ = self.os_cli.split_frontmatter(workflow_path)
            for target in metadata.get("next_workflows", []):
                if target == "none":
                    continue
                self.assertIn(target, profiles, msg=f"Unknown workflow route: {record['id']} -> {target}")
                self.assertIn(
                    "general",
                    profiles[target],
                    msg=f"General workflow {record['id']} depends on spatial-only {target}",
                )

    def test_active_spatial_guidance_does_not_reintroduce_compulsory_legacy_rules(self) -> None:
        roots = [GLOBAL / "skills" / name for name in AFFECTED_SKILLS]
        roots.append(GLOBAL / "skills" / "ui-ux" / "reference" / "spatial-ui-system.md")
        roots.extend(
            [
                GLOBAL / "workflows" / "workflow-spatial-project-inception.md",
                GLOBAL / "skills" / "spatial-experience-design" / "reference" / "project-phase-routing.md",
            ]
        )
        files: list[Path] = []
        for root in roots:
            files.extend(root.rglob("*.md") if root.is_dir() else [root])
        corpus = "\n".join(read(path).lower() for path in files)
        forbidden = (
            "must select an elite effect",
            "must first consult the global motion library",
            "all spatial concept artifacts exist",
            "ui follows atmosphere -> taste -> transformation -> proof -> method -> inquiry",
            "story follows atmosphere -> taste -> transformation -> proof -> method -> inquiry",
            "every beat has an anchor object or is explicitly marked as a risk zone",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, corpus)


    def test_v5_working_records_do_not_require_a_fixed_file_set(self) -> None:
        inception = read(GLOBAL / "workflows" / "workflow-spatial-project-inception.md")
        spatial_skill = read(GLOBAL / "skills" / "spatial-experience-design" / "SKILL.md")
        self.assertIn("Working records, kept light", inception)
        self.assertIn("Do not create files to satisfy a file count", inception)
        self.assertIn("Do not generate paperwork", spatial_skill)
        for filename in CORE_ARTIFACTS:
            self.assertTrue((GLOBAL / "context_templates" / filename).is_file())


    def test_spatial_inception_is_director_led_and_conversational(self) -> None:
        inception = read(GLOBAL / "workflows" / "workflow-spatial-project-inception.md")
        studio_director = read(GLOBAL / "agents" / "studio-director" / "AGENT.md")
        design_director = read(GLOBAL / "agents" / "design-director" / "AGENT.md")
        self.assertIn("Three working loops", inception)
        self.assertIn("not stages that must be completed in order", inception)
        self.assertIn("The designer can interrupt, redirect, reject, or choose", inception)
        self.assertIn("Do not restart inception merely because", inception)
        self.assertIn("do not make Beloved invoke a workflow", " ".join(studio_director.split()))
        self.assertIn("functional design owner", design_director)


    def test_spatial_route_handoffs_and_specialist_ownership_are_explicit(self) -> None:
        inception = read(GLOBAL / "workflows" / "workflow-spatial-project-inception.md")
        phase_router = read(GLOBAL / "skills" / "spatial-experience-design" / "reference" / "project-phase-routing.md")
        design_director = read(GLOBAL / "agents" / "design-director" / "AGENT.md")
        global_router = read(GLOBAL / "GLOBAL_MEMORY.md")
        corpus = "\n".join((inception, phase_router, design_director, global_router))
        for phrase in ("current route and lens", "selected/loaded/used", "next route", "return condition"):
            self.assertIn(phrase, corpus)
        for route in ("ui-ux", "media-choreography", "cinematic-motion", "scroll-storyboard", "motion-library", "canvas-ui", "reference-intelligence", "video-generation", "prompt-engineering"):
            self.assertIn(route, inception)
        self.assertIn("functional design owner", design_director)
        self.assertIn("conditional critique and gate method", design_director)
        self.assertIn("master-design-director", global_router)
        self.assertIn("does not impose a house aesthetic", inception)


    def test_v5_keeps_prior_site_and_scroll_verification_resources(self) -> None:
        spatial_skill = read(GLOBAL / "skills" / "spatial-experience-design" / "SKILL.md")
        grammar = read(GLOBAL / "skills" / "spatial-experience-design" / "reference" / "page-grammar-and-fingerprint.md")
        storytelling = read(GLOBAL / "skills" / "storytelling" / "SKILL.md")
        storyboard = read(GLOBAL / "skills" / "scroll-storyboard" / "SKILL.md")
        motion = read(GLOBAL / "skills" / "cinematic-motion" / "SKILL.md")
        scroll_verification = read(GLOBAL / "skills" / "cinematic-motion" / "reference" / "scroll-verification.md")
        production_plan = read(GLOBAL / "context_templates" / "production-plan.md")
        template_ids = {record["id"] for record in self.manifest["context_templates"]}
        self.assertIn("page-grammar-and-fingerprint.md", spatial_skill)
        self.assertIn("site-fingerprints.md", spatial_skill)
        self.assertIn("site-fingerprints", template_ids)
        self.assertIn("Grammar forbids", grammar)
        self.assertIn("A feeling curve is optional", storytelling)
        self.assertIn("cold-scroll", storytelling)
        self.assertIn("primary remembered peak", storyboard)
        self.assertIn("scroll-verification.md", motion)
        for check in ("Dead scroll", "Frozen media", "Composited contrast", "Focus and reachability", "Mobile and reduced motion", "contact sheet", "cold scroll"):
            self.assertIn(check, scroll_verification)
        self.assertIn("keyframe interval/GOP", production_plan)
        self.assertNotIn("--sc-p", "\n".join((grammar, storytelling, storyboard, motion, scroll_verification)))


    def test_focused_spatial_questions_remain_direct_skills(self) -> None:
        workflow_ids = {record["id"] for record in self.manifest["workflows"]}
        phase_router = read(GLOBAL / "skills" / "spatial-experience-design" / "reference" / "project-phase-routing.md")
        fixture = json.loads(read(REPO_ROOT / "tests" / "fixtures" / "routing.json"))
        scenarios = {scenario["id"]: scenario for scenario in fixture["scenarios"]}
        for filename in RETIRED_SPATIAL_ROUTE_FILES:
            self.assertFalse((GLOBAL / "workflows" / filename).exists())
            self.assertNotIn(filename.removeprefix("workflow-").removesuffix(".md"), workflow_ids)
        self.assertIn("spatial-project-inception", workflow_ids)
        self.assertIn("Focused phase routing", phase_router)
        expected_direct_routes = {
            "spatial-reference-analysis": "reference-intelligence",
            "spatial-concept-directions": "spatial-experience-design",
            "spatial-concept-selection": "spatial-experience-design",
            "spatial-story-development": "storytelling",
            "spatial-ui-vertical-slice": "ui-ux",
            "spatial-motion-design": "cinematic-motion",
            "v5-spatial-media-feasibility": "media-choreography",
        }
        for scenario_id, skill_id in expected_direct_routes.items():
            self.assertEqual("skill", scenarios[scenario_id]["route_kind"])
            self.assertEqual(skill_id, scenarios[scenario_id]["route"])
            self.assertEqual(["spatial"], scenarios[scenario_id]["active_packs"])
            self.assertEqual("read_only", scenarios[scenario_id]["maximum_mutation_class"])
        self.assertIn("Explore whole-page concept directions", phase_router)
        self.assertIn("Compare and select a territory", phase_router)
        self.assertIn("risk prototype first", phase_router)

    def test_every_affected_skill_resource_is_reachable_from_a_router(self) -> None:
        for name in AFFECTED_SKILLS:
            root = GLOBAL / "skills" / name
            routers = [root / "SKILL.md"]
            routers.extend(root.glob("reference*/resource-index.md"))
            router_text = "\n".join(read(path) for path in routers if path.exists())
            resources = [
                path
                for path in root.rglob("*.md")
                if path.name != "SKILL.md"
                and path not in routers
                and "agents" not in path.parts
            ]
            for resource in resources:
                self.assertIn(
                    resource.name,
                    router_text,
                    msg=f"{resource.relative_to(REPO_ROOT)} is not routed from its skill or resource index",
                )

    def test_six_behavioral_paper_traces_cover_required_decisions(self) -> None:
        fixture = json.loads(read(REPO_ROOT / "tests" / "fixtures" / "spatial_behavior_scenarios.json"))
        scenarios = fixture["scenarios"]
        self.assertEqual(6, len(scenarios))
        required = {
            "selected_skills",
            "workflow",
            "files_loaded",
            "conversation_sequence",
            "artifacts",
            "approval_gates",
            "optional_complexity",
            "expected_handoff",
        }
        for scenario in scenarios:
            self.assertTrue(required.issubset(scenario))
            self.assertTrue(scenario["conversation_sequence"])
            self.assertTrue(scenario["approval_gates"])
        saas = next(item for item in scenarios if item["id"] == "general-saas-unaffected")
        self.assertEqual("project-inception", saas["workflow"])
        self.assertEqual("rejected", saas["optional_complexity"]["spatial-profile"])


if __name__ == "__main__":
    unittest.main()
