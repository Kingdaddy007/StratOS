from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
COMPETITOR_ROOT = REPO_ROOT / "global" / "skills" / "competitor-profiling"


class PromptSevenCompetitorIntelligenceRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = (COMPETITOR_ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.evidence = (
            COMPETITOR_ROOT / "references" / "evidence-and-source-record.md"
        ).read_text(encoding="utf-8")
        cls.tools = (COMPETITOR_ROOT / "references" / "tool-reference.md").read_text(
            encoding="utf-8"
        )
        cls.index = (COMPETITOR_ROOT / "references" / "resource-index.md").read_text(
            encoding="utf-8"
        )

    def test_activation_and_question_first_routing(self) -> None:
        self.assertIn("competitive intelligence", self.skill)
        self.assertIn("State the decision the research will support", self.skill)
        self.assertIn("quick_scan", self.skill)
        self.assertIn("freshness requirement", self.skill)

    def test_collection_is_capability_first_and_no_provider_assumption(self) -> None:
        self.assertIn("Never require a named scraping", self.skill)
        self.assertIn("Inspect available read-only capabilities", self.skill)
        self.assertIn("Do not assume a named provider is installed", self.skill)
        self.assertIn("Discover capabilities at runtime", self.tools)
        self.assertNotIn("Firecrawl", self.skill)
        self.assertNotIn("DataForSEO", self.skill)

    def test_access_and_privacy_boundaries_are_explicit(self) -> None:
        for phrase in (
            "Never bypass authentication",
            "Never collect, persist, or expose personal data",
            "robots.txt as authentication",
            "report unknown",
        ):
            self.assertIn(phrase, self.skill)
        self.assertIn("not access authorization", self.evidence)
        self.assertIn("public data remains subject to privacy", self.evidence)

    def test_claim_provenance_and_fair_comparison_are_required(self) -> None:
        self.assertIn("Label every material statement", self.skill)
        self.assertIn("observation`, `source_reported_claim`", self.skill)
        self.assertIn("Compare like with like", self.skill)
        self.assertIn("Claim ID and wording", self.evidence)
        self.assertIn("regional, temporal, product-tier", self.skill)

    def test_references_and_output_are_auditable(self) -> None:
        self.assertIn("evidence-and-source-record.md", self.index)
        self.assertIn("templates.md", self.index)
        self.assertIn("RFC 9309", self.index)
        self.assertIn("2026-08-19", self.index)
        self.assertIn("Evidence ledger", self.skill)
        self.assertIn("Decision handoff", self.skill)

    def test_eval_fixture_has_positive_and_negative_boundaries(self) -> None:
        evals = json.loads(
            (COMPETITOR_ROOT / "evals" / "evals.json").read_text(encoding="utf-8")
        )
        ids = {entry["id"] for entry in evals["evals"]}
        self.assertEqual(
            ids,
            {
                "question-first-scan",
                "tool-agnostic-fallback",
                "robots-and-access-boundary",
                "claim-provenance",
                "fair-comparison",
                "external-publication-boundary",
            },
        )


if __name__ == "__main__":
    unittest.main()
