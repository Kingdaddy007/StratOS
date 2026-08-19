from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SALES_ROOT = REPO_ROOT / "global" / "skills" / "sales-enablement"


class PromptFiveEthicalSalesEnablementRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = (SALES_ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.claim_reference = (
            SALES_ROOT / "references" / "claim-governance-and-approval.md"
        ).read_text(encoding="utf-8")
        cls.deck_reference = (
            SALES_ROOT / "references" / "deck-frameworks.md"
        ).read_text(encoding="utf-8")
        cls.index = (SALES_ROOT / "references" / "resource-index.md").read_text(
            encoding="utf-8"
        )
        cls.evals = json.loads(
            (SALES_ROOT / "evals" / "evals.json").read_text(encoding="utf-8")
        )

    def test_claim_provenance_and_audience_interpretation_are_required(self) -> None:
        self.assertIn("compact claim ledger", self.skill)
        self.assertIn("client assertion remains an assertion", self.skill)
        self.assertIn("likely audience interpretation", self.skill)
        self.assertIn("Claim ID and exact wording", self.claim_reference)
        self.assertIn("including implications and omissions", self.claim_reference)

    def test_deck_shape_and_sales_sequence_are_not_universal_rules(self) -> None:
        self.assertIn("Do not impose a slide count, a fixed sequence", self.skill)
        self.assertIn("Select the smallest useful format", self.skill)
        self.assertIn("Start with the decision, not a slide count", self.deck_reference)
        self.assertNotIn("10-12 Slide Framework", self.deck_reference)

    def test_personas_and_value_models_remain_evidence_bound(self) -> None:
        self.assertIn("as hypotheses", self.skill)
        self.assertIn("labelled estimate or illustrative scenario", self.skill)
        self.assertIn("range or sensitivity", self.skill)
        self.assertIn("Call it an estimate, never a promise", self.claim_reference)

    def test_proof_and_external_effects_are_approval_gated(self) -> None:
        self.assertIn("Confirm provenance and permission", self.skill)
        self.assertIn("just-in-time human approval", self.skill)
        self.assertIn("exact version, channel, named approver", self.claim_reference)
        self.assertIn("Do not publish or send it", self.claim_reference)

    def test_resources_and_evals_cover_required_positive_and_negative_paths(self) -> None:
        self.assertIn("claim-governance-and-approval.md", self.index)
        self.assertIn("FTC Advertising FAQ", self.index)
        self.assertIn("2026-08-19", self.index)
        ids = {entry["id"] for entry in self.evals["evals"]}
        self.assertEqual(
            ids,
            {
                "fit-for-purpose-deck",
                "client-assertion-case-study",
                "value-model-scenario",
                "ethical-objection-support",
                "outbound-boundary",
                "public-comparison-boundary",
            },
        )


if __name__ == "__main__":
    unittest.main()
