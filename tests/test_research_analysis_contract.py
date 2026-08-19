from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "global" / "skills" / "research-analysis"


class ResearchAnalysisContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.openai = (SKILL_ROOT / "agents" / "openai.yaml").read_text(
            encoding="utf-8"
        )
        cls.evals = json.loads(
            (SKILL_ROOT / "evals" / "evals.json").read_text(encoding="utf-8")
        )

    def test_activation_exclusions_and_modes_are_explicit(self) -> None:
        for phrase in (
            "decision-relevant research",
            "Do not load for simple factual lookup",
            "quick_scan",
            "capability_audit",
            "multi_report_synthesis",
            "host_probe",
        ):
            self.assertIn(phrase, self.skill)

    def test_evidence_grading_and_claim_labels_are_required(self) -> None:
        for phrase in (
            "Grade | Prefer | Use",
            "`observed`",
            "`source_reported_claim`",
            "`inference`",
            "`hypothesis`",
            "`recommendation`",
            "`unknown`",
            "source, URL/path, access or publication date",
        ):
            self.assertIn(phrase, self.skill)

    def test_falsification_synthesis_and_stopping_are_required(self) -> None:
        for phrase in (
            "RESEARCH AND FALSIFICATION LOOP",
            "failure reports, post-mortems, abandonment reasons",
            "When comparing reports",
            "STOPPING RULE",
            "Further research is unlikely to change the decision",
        ):
            self.assertIn(phrase, self.skill)

    def test_authority_boundary_and_output_contract_are_present(self) -> None:
        for phrase in (
            "Do not convert research into implementation",
            "## OUTPUT SHAPE",
            "Evidence Ledger",
            "Invalidating condition / re-evaluation date",
            "Never turn research into permission",
        ):
            self.assertIn(phrase, self.skill)
        self.assertIn("source grading, falsification, and stopping rules", self.openai)

    def test_eval_fixture_has_positive_and_negative_boundaries(self) -> None:
        ids = {entry["id"] for entry in self.evals["evals"]}
        self.assertEqual(
            ids,
            {
                "question-first-comparison",
                "source-and-claim-labels",
                "adversarial-falsification",
                "multi-report-synthesis",
                "stopping-and-no-new-skill",
                "authority-boundary",
            },
        )
        self.assertTrue(any("deployment" in e["prompt"] for e in self.evals["evals"]))


if __name__ == "__main__":
    unittest.main()
