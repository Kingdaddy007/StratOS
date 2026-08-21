from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "global" / "scripts" / "os.py"
DRILLS_PATH = REPO_ROOT / "tests" / "fixtures" / "v4_phase_6_integration_drills.json"


def load_os_module():
    spec = importlib.util.spec_from_file_location("antigravity_os_cli_phase_6", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load Anti-Gravity OS CLI")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PhaseSixIntegrationDrillTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.os_cli = load_os_module()
        cls.drills = json.loads(DRILLS_PATH.read_text(encoding="utf-8"))["drills"]

    def workflow_metadata(self, workflow_id: str) -> tuple[dict, str]:
        path = REPO_ROOT / "global" / "workflows" / f"workflow-{workflow_id}.md"
        text = path.read_text(encoding="utf-8")
        _, frontmatter, body = text.split("---", 2)
        return self.os_cli.parse_simple_yaml(frontmatter), body

    def skill_text(self, skill_id: str) -> str:
        return (REPO_ROOT / "global" / "skills" / skill_id / "SKILL.md").read_text(
            encoding="utf-8"
        )

    def test_drills_are_unique_and_reference_existing_assets(self) -> None:
        ids = [drill["id"] for drill in self.drills]
        self.assertEqual(len(ids), len(set(ids)))

        for drill in self.drills:
            for skill_id in drill["required_skills"]:
                self.assertTrue(
                    (REPO_ROOT / "global" / "skills" / skill_id / "SKILL.md").is_file(),
                    drill["id"],
                )
            for resource in drill["conditional_resources"]:
                if resource in {"architecture", "security", "testing"}:
                    self.assertTrue(
                        (REPO_ROOT / "global" / "skills" / resource / "SKILL.md").is_file(),
                        drill["id"],
                    )
                else:
                    self.assertTrue(
                        (REPO_ROOT / "global" / "skills" / resource).is_file(), drill["id"]
                    )

    def test_each_declared_workflow_handoff_is_exposed_by_the_entry_route(self) -> None:
        for drill in self.drills:
            workflow_id = drill["entry_workflow"]
            if workflow_id is None:
                continue
            metadata, _ = self.workflow_metadata(workflow_id)
            for handoff in drill["required_handoffs"]:
                self.assertIn(handoff, metadata["next_workflows"], drill["id"])

    def test_uncertain_ai_product_stays_decision_first_and_read_only(self) -> None:
        metadata, body = self.workflow_metadata("project-inception")
        product = self.skill_text("product-thinking")

        self.assertEqual("read_only", metadata["mutation_class"])
        self.assertIn("decision-ready first-direction workflow", body)
        self.assertIn("It may produce a proposed packet and route", body)
        self.assertIn("Compare the simplest non-AI", product)
        self.assertIn("does not create project contexts", body)

    def test_diagnosis_and_flaky_drills_stop_before_repair_or_retry(self) -> None:
        _, debug_body = self.workflow_metadata("debug-issue")
        testing = self.skill_text("testing")

        self.assertIn("No source/test edit.", debug_body)
        self.assertIn("Enter `implement` only when:", debug_body)
        self.assertIn("retry until green", testing)
        self.assertIn("Use `debugging` for a failing or flaky result", testing)

    def test_test_strategy_remains_a_read_only_plan_until_implement_is_authorized(self) -> None:
        _, body = self.workflow_metadata("test-strategy")

        self.assertIn("`propose`", body)
        self.assertIn("it edits tests only in explicitly requested `implement` mode", body)
        self.assertIn("smallest credible evidence", body)
        self.assertIn("retry success is not diagnosis", body)

    def test_material_build_routes_workflows_without_requiring_user_vocabulary(self) -> None:
        metadata, build_feature = self.workflow_metadata("build-feature")
        router = (REPO_ROOT / "global" / "GLOBAL_MEMORY.md").read_text(encoding="utf-8")
        director = (
            REPO_ROOT / "global" / "agents" / "studio-director" / "AGENT.md"
        ).read_text(encoding="utf-8")
        drill = next(
            item for item in self.drills if item["id"] == "automatically-routed-material-build"
        )

        self.assertEqual("build-feature", drill["entry_workflow"])
        self.assertNotIn("workflow", drill["prompt_shape"].lower())
        self.assertIn("task-dispatch", metadata["next_workflows"])
        self.assertIn("acceptance-gate and dispatch decision", metadata["outputs"][2])
        self.assertIn("The user does not need to name these workflows", build_feature)
        self.assertIn("Beloved never needs to name a workflow", router)
        self.assertIn("Beloved does not need to remember or invoke workflow names", director)

    def test_ai_evaluation_and_release_drills_keep_security_and_production_separate(self) -> None:
        _, test_strategy = self.workflow_metadata("test-strategy")
        _, verify_project = self.workflow_metadata("verify-project")
        testing = self.skill_text("testing")

        self.assertIn("security-audit", test_strategy)
        self.assertIn("LLM judge as the sole oracle", testing)
        self.assertIn("read-only evidence-gathering", verify_project)
        self.assertIn("ship-to-production", verify_project)
        self.assertIn("cannot substitute for missing tests or authorize deployment", verify_project)

    def test_small_reversible_change_is_not_forced_through_a_phase_six_route(self) -> None:
        router = (REPO_ROOT / "global" / "GLOBAL_MEMORY.md").read_text(encoding="utf-8")
        product = self.skill_text("product-thinking")

        self.assertIn("No route is mandatory for a small reversible task", router)
        self.assertIn("Turn a clear, reversible, low-consequence change", product)


if __name__ == "__main__":
    unittest.main()
