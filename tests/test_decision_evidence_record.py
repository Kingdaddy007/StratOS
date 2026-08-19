from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = REPO_ROOT / "global" / "global_templates" / "decision-evidence-record.md"


class DecisionEvidenceRecordTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = TEMPLATE.read_text(encoding="utf-8")

    def test_record_supports_all_studio_decision_domains(self) -> None:
        for domain in (
            "product",
            "design",
            "architecture",
            "engineering",
            "assurance",
            "research",
            "growth",
        ):
            self.assertIn(domain, self.text)

    def test_record_preserves_evidence_and_uncertainty(self) -> None:
        for phrase in (
            "Decision owner",
            "Consequence of being wrong",
            "Decision criteria",
            "Baseline",
            "Evidence ledger",
            "source_reported_claim",
            "Strongest contrary evidence",
            "Stopping condition",
            "Invalidating condition",
            "Approval required",
            "superseding record",
        ):
            self.assertIn(phrase, self.text)

    def test_record_does_not_grant_authority(self) -> None:
        self.assertIn("A recommendation does not authorise implementation", self.text)


if __name__ == "__main__":
    unittest.main()
