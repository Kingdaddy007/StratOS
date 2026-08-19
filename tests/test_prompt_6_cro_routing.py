from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CRO_ROOT = REPO_ROOT / "global" / "skills" / "page-cro"


class PromptSixCRORoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = (CRO_ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.reference = (
            CRO_ROOT / "references" / "evidence-and-method-selection.md"
        ).read_text(encoding="utf-8")
        cls.experiments = (CRO_ROOT / "references" / "experiments.md").read_text(
            encoding="utf-8"
        )
        cls.index = (CRO_ROOT / "references" / "resource-index.md").read_text(
            encoding="utf-8"
        )
        cls.evals = json.loads(
            (CRO_ROOT / "evals" / "evals.json").read_text(encoding="utf-8")
        )

    def test_activation_and_decision_context_are_explicit(self) -> None:
        self.assertIn("conversion", self.skill)
        self.assertIn("fresh copy draft", self.skill)
        self.assertIn("Define the decision, user task", self.skill)
        self.assertIn("consequence of being wrong", self.reference)

    def test_old_cro_slogans_are_not_universal_rules(self) -> None:
        for phrase in (
            "five seconds",
            "above the fold",
            "one CTA",
            "no navigation",
            "fewer fields",
        ):
            self.assertIn(phrase, self.skill)
        self.assertIn("conditional design choices", self.skill)
        self.assertNotIn("Every landing page needs one CTA", self.skill)

    def test_method_and_measurement_gates_are_present(self) -> None:
        self.assertIn("verify event structure and live firing", self.skill)
        self.assertIn("Choose the least costly valid method", self.skill)
        self.assertIn("falsifiable hypothesis", self.skill)
        self.assertIn("exposure unit", self.reference)
        self.assertIn("Report inconclusive", self.reference)

    def test_accessibility_privacy_and_autonomy_are_safety_boundaries(self) -> None:
        self.assertIn("ACCESSIBILITY, AUTONOMY, AND PRIVACY GATE", self.skill)
        self.assertIn("Never hide material costs", self.skill)
        self.assertIn("Correct and verify known defect", self.skill)
        self.assertIn("false urgency", self.reference)
        self.assertIn("obstructed cancellation", self.skill)

    def test_references_and_evals_are_selectively_routed(self) -> None:
        self.assertIn("evidence-and-method-selection.md", self.index)
        self.assertIn("experiments.md", self.index)
        self.assertIn("WCAG 2.2", self.index)
        self.assertIn("2026-08-19", self.index)
        ids = {entry["id"] for entry in self.evals["evals"]}
        self.assertEqual(
            ids,
            {
                "decision-first-diagnosis",
                "conditional-layout-rules",
                "measurement-integrity",
                "method-selection",
                "accessibility-remediation",
                "autonomy-boundary",
            },
        )
