from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def skill(skill_id: str) -> str:
    return (REPO_ROOT / "global" / "skills" / skill_id / "SKILL.md").read_text(
        encoding="utf-8"
    )


class PromptTwoApiDataRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api = skill("api-design")
        cls.database = skill("database")
        cls.api_reference = (
            REPO_ROOT
            / "global"
            / "skills"
            / "api-design"
            / "references"
            / "extended-guidance.md"
        ).read_text(encoding="utf-8")
        cls.database_reference = (
            REPO_ROOT
            / "global"
            / "skills"
            / "database"
            / "references"
            / "extended-guidance.md"
        ).read_text(encoding="utf-8")

    def test_api_drops_universal_version_pagination_and_rate_limit_rules(self) -> None:
        self.assertIn("merely because every API is assumed to need one", self.api)
        self.assertIn("proven safe bound or an explicit limit", self.api)
        self.assertIn("Do not add arbitrary throttles", self.api)
        self.assertNotIn("Deploy an API without versioning from day one", self.api)
        self.assertNotIn("all collection endpoints must be paginated", self.api)

    def test_api_requires_owner_consumer_and_contract_discrepancy_analysis(self) -> None:
        self.assertIn("Owner and known consumers:", self.api)
        self.assertIn("Classify disagreement as stale artifact", self.api)
        self.assertIn("do not choose the most convenient artifact", self.api)
        self.assertIn("discrepancy record", self.api_reference)

    def test_api_treats_tenant_and_retry_as_real_boundary_decisions(self) -> None:
        self.assertIn("object, tenant, function, and protected-property", self.api)
        self.assertIn("timeout/replay case", self.api)
        self.assertIn("Do not claim exactly-once delivery", self.api_reference)
        self.assertIn("wrong-tenant", self.api_reference)

    def test_database_drops_false_universal_defaults(self) -> None:
        self.assertIn("as a universal default", self.database)
        self.assertNotIn("Start at 3NF", self.database)
        self.assertNotIn("Design for a Billion Rows", self.database)
        self.assertNotIn("Prefer soft deletes", self.database)
        self.assertIn("prefer keeping it", self.database)

    def test_database_requires_invariants_lifecycle_and_recovery_reasoning(self) -> None:
        self.assertIn("place enforcement at the strongest practical boundary", self.database)
        self.assertIn("Treat identity separately from lifecycle", self.database)
        self.assertIn("code rollback as proof", self.database)
        self.assertIn("Current and desired shape:", self.database_reference)
        self.assertIn("Do not claim legal compliance", self.database_reference)

    def test_api_and_database_keep_high_consequence_execution_gated(self) -> None:
        self.assertIn("does not authorize deployment", self.api)
        self.assertIn("does not grant approval to mutate data", self.database)
        self.assertIn("database-migration", self.database)
        self.assertIn("just-in-time human approval", self.database_reference)


if __name__ == "__main__":
    unittest.main()
