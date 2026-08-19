from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class V4PrivatePilotFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = json.loads(
            (REPO_ROOT / "tests" / "fixtures" / "v4_private_pilot.json").read_text(
                encoding="utf-8"
            )
        )
        self.manifest = json.loads(
            (REPO_ROOT / "global" / "manifest.yaml").read_text(encoding="utf-8")
        )

    def test_fixture_has_ten_distinct_cases_and_no_trading_route(self) -> None:
        cases = self.fixture["scenarios"]
        self.assertEqual(10, len(cases))
        self.assertEqual(10, len({case["id"] for case in cases}))
        self.assertNotIn("trading", " ".join(case["expected_route"] for case in cases).lower())

    def test_expected_routes_are_live_and_profiles_are_registered(self) -> None:
        live_workflows = {entry["id"] for entry in self.manifest["workflows"]}
        live_skills = {entry["id"] for entry in self.manifest["skills"]}
        profiles = set(self.manifest["profiles"])
        for case in self.fixture["scenarios"]:
            self.assertIn(case["expected_profile"], profiles)
            self.assertIn(case["expected_route"], live_workflows | live_skills)

    def test_release_case_requires_approval_and_external_mutation_class(self) -> None:
        release = next(case for case in self.fixture["scenarios"] if case["id"] == "release-stop")
        self.assertTrue(release["approval_required"])
        self.assertEqual("external_or_production", release["expected_mutation_class"])
        for case in self.fixture["scenarios"]:
            if case["id"] != "release-stop":
                expected = "local_edit" if case["id"] == "ordinary-approved-feature" else "read_only"
                self.assertEqual(expected, case["expected_mutation_class"])


if __name__ == "__main__":
    unittest.main()
