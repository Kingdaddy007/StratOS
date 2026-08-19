from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_PATH = REPO_ROOT / "tests" / "fixtures" / "architecture_capability_evals.json"


def load_fixture() -> dict:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


class ArchitectureCapabilityEvaluationContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = load_fixture()

    def test_suite_identity_and_conditions_are_explicit(self) -> None:
        self.assertEqual("1.0", self.fixture["schema_version"])
        self.assertEqual("architecture-capability-abc-v1", self.fixture["suite_id"])
        self.assertEqual({"A", "B", "C"}, set(self.fixture["conditions"]))
        self.assertTrue(self.fixture["kernel"]["instructions"])
        for description in self.fixture["conditions"].values():
            self.assertIsInstance(description, str)
            self.assertGreater(len(description.strip()), 40)

    def test_weighted_rubric_is_complete_and_balanced(self) -> None:
        dimensions = self.fixture["dimensions"]
        identifiers = [dimension["id"] for dimension in dimensions]

        self.assertEqual(len(identifiers), len(set(identifiers)))
        self.assertEqual(100, sum(dimension["weight"] for dimension in dimensions))
        self.assertIn("correctness", identifiers)
        self.assertIn("failure_mode_detection", identifiers)
        self.assertIn("security_and_data_integrity", identifiers)
        self.assertIn("complexity_discipline", identifiers)
        self.assertIn("instruction_flexibility", identifiers)
        self.assertIn("adjacent_task_safety", identifiers)

        for dimension in dimensions:
            self.assertGreater(dimension["weight"], 0)
            self.assertIs(dimension["higher_is_better"], True)
            self.assertTrue(dimension["judge"].strip())

    def test_candidate_specs_have_activation_exclusion_and_boxing_boundaries(self) -> None:
        candidates = self.fixture["candidates"]
        candidate_ids = [candidate["id"] for candidate in candidates]

        self.assertEqual(4, len(candidates))
        self.assertEqual(len(candidate_ids), len(set(candidate_ids)))

        for candidate in candidates:
            for field in (
                "title",
                "target_failure",
                "activation",
                "exclusions",
                "boxing_risk",
            ):
                self.assertTrue(candidate[field].strip(), f"{candidate['id']} missing {field}")
            self.assertGreaterEqual(len(candidate["instructions"]), 4)

    def test_nine_scenarios_cover_candidates_adversary_and_adjacent_control(self) -> None:
        scenarios = self.fixture["scenarios"]
        scenario_ids = [scenario["id"] for scenario in scenarios]
        candidate_ids = {candidate["id"] for candidate in self.fixture["candidates"]}
        covered_candidates = {
            scenario["candidate_id"]
            for scenario in scenarios
            if scenario["candidate_id"] is not None
        }

        self.assertEqual(9, len(scenarios))
        self.assertEqual(len(scenario_ids), len(set(scenario_ids)))
        self.assertEqual(candidate_ids, covered_candidates)
        self.assertIn("adversarial", {scenario["kind"] for scenario in scenarios})
        self.assertIn("adjacent_control", {scenario["kind"] for scenario in scenarios})

    def test_safe_contract_candidate_has_conflict_and_anti_boxing_controls(self) -> None:
        candidate = next(
            item
            for item in self.fixture["candidates"]
            if item["id"] == "safe-contract-evolution"
        )
        scenarios = {scenario["id"]: scenario for scenario in self.fixture["scenarios"]}
        conflict = scenarios["live-contract-conflicting-write"]
        control = scenarios["disposable-contract-rename-control"]

        self.assertIn("Apply the remaining instructions only", candidate["instructions"][0])
        self.assertIn("omit contract-migration analysis", candidate["instructions"][0])
        self.assertEqual("safe-contract-evolution", conflict["candidate_id"])
        self.assertIs(conflict["expected_architecture_activation"], True)
        self.assertIn("different values", conflict["task_prompt"])
        self.assertEqual("safe-contract-evolution", control["candidate_id"])
        self.assertIs(control["expected_architecture_activation"], False)
        self.assertEqual("anti_boxing", control["kind"])

    def test_network_effects_candidate_has_an_explicit_non_activation_rule(self) -> None:
        candidate = next(
            item
            for item in self.fixture["candidates"]
            if item["id"] == "network-effects-safety"
        )

        self.assertIn("Before applying this capability", candidate["instructions"][0])
        self.assertIn("do not add retry", candidate["instructions"][0])

    def test_tenant_candidate_has_a_direct_single_tenant_control(self) -> None:
        candidate = next(
            item
            for item in self.fixture["candidates"]
            if item["id"] == "tenant-trust-boundaries"
        )
        scenarios = {scenario["id"]: scenario for scenario in self.fixture["scenarios"]}
        control = scenarios["single-company-access-control"]

        self.assertIn("Before applying this capability", candidate["instructions"][0])
        self.assertIn("do not add tenant", candidate["instructions"][0])
        self.assertEqual("tenant-trust-boundaries", control["candidate_id"])
        self.assertEqual("anti_boxing", control["kind"])
        self.assertIs(control["expected_architecture_activation"], False)
        self.assertIn("one company", control["task_prompt"])

    def test_each_scenario_is_evaluable_without_prescribing_implementation(self) -> None:
        valid_dimensions = {dimension["id"] for dimension in self.fixture["dimensions"]}
        candidate_ids = {candidate["id"] for candidate in self.fixture["candidates"]}

        for scenario in self.fixture["scenarios"]:
            self.assertIsInstance(scenario["expected_architecture_activation"], bool)
            self.assertTrue(scenario["candidate_ids_to_test"])
            self.assertTrue(set(scenario["candidate_ids_to_test"]).issubset(candidate_ids))
            self.assertGreater(len(scenario["task_prompt"].strip()), 80)
            self.assertGreaterEqual(len(scenario["hidden_evaluator_risks"]), 2)
            self.assertGreaterEqual(len(scenario["required_observations"]), 3)
            self.assertGreaterEqual(len(scenario["forbidden_overreach"]), 2)
            self.assertTrue(scenario["scoring_focus"])
            self.assertTrue(set(scenario["scoring_focus"]).issubset(valid_dimensions))

    def test_adjacent_control_keeps_architecture_inactive(self) -> None:
        adjacent = [
            scenario
            for scenario in self.fixture["scenarios"]
            if scenario["kind"] == "adjacent_control"
        ]

        self.assertEqual(1, len(adjacent))
        self.assertIs(adjacent[0]["expected_architecture_activation"], False)
        self.assertIsNone(adjacent[0]["candidate_id"])
        self.assertEqual(
            {candidate["id"] for candidate in self.fixture["candidates"]},
            set(adjacent[0]["candidate_ids_to_test"]),
        )
        self.assertIn("adjacent_task_safety", adjacent[0]["scoring_focus"])

    def test_fixture_contains_no_unresolved_template_tokens(self) -> None:
        raw = FIXTURE_PATH.read_text(encoding="utf-8")
        self.assertNotIn("{{", raw)
        self.assertNotIn("}}", raw)


if __name__ == "__main__":
    unittest.main()
