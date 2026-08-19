from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def skill(skill_id: str) -> str:
    return (REPO_ROOT / "global" / "skills" / skill_id / "SKILL.md").read_text(
        encoding="utf-8"
    )


class PromptOneEngineeringRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.coding = skill("coding")
        cls.refactoring = skill("refactoring")
        cls.review = skill("review-audit")
        cls.refactoring_reference = (
            REPO_ROOT
            / "global"
            / "skills"
            / "refactoring"
            / "references"
            / "extended-guidance.md"
        ).read_text(encoding="utf-8")
        cls.review_reference = (
            REPO_ROOT
            / "global"
            / "skills"
            / "review-audit"
            / "references"
            / "change-scope-and-handoff.md"
        ).read_text(encoding="utf-8")

    def test_fixed_numeric_and_git_rules_are_not_universal(self) -> None:
        self.assertNotIn("≤3 parameters", self.coding)
        self.assertNotIn("fewer than 3 concrete cases", self.coding)
        self.assertNotIn("always use three-dot", self.review)
        self.assertIn("not a universal review rule", self.review_reference)

    def test_nontrivial_change_requires_risk_matched_record_and_evidence(self) -> None:
        for expected in (
            "Objective:",
            "Non-goals:",
            "Highest-risk assumption:",
            "Evidence plan:",
            "Recovery limit and approval boundary:",
        ):
            self.assertIn(expected, self.coding)
        self.assertIn("Choose evidence for the plausible failure surface", self.coding)
        self.assertIn("Do not create ceremony for a harmless local edit", self.coding)

    def test_refactor_repair_and_legacy_routes_remain_explicit(self) -> None:
        self.assertIn("Separate by default", self.refactoring)
        self.assertIn("Combine only when the repair depends", self.refactoring)
        self.assertIn("observe and characterize relevant current behaviour", self.refactoring)
        self.assertIn("current behaviour", self.refactoring_reference)
        self.assertIn("not as a statement that the behaviour is correct", self.refactoring_reference)

    def test_review_uses_actual_base_handoff_and_risk_sized_stopping(self) -> None:
        self.assertIn("actual review comparison", self.review)
        self.assertIn("reconstruct the change surface independently", self.review)
        self.assertIn("Do not make an unavailable second agent a hard blocker", self.review)
        self.assertIn("Stop when the meaningful failure surface", self.review)
        self.assertIn("three-dot comparison can be useful", self.review_reference)

    def test_high_consequence_boundaries_stop_before_external_effect(self) -> None:
        self.assertIn("Do not execute", self.coding)
        self.assertIn("required human approval", self.coding)
        self.assertIn("cannot invent human authorization", self.review_reference)


if __name__ == "__main__":
    unittest.main()
