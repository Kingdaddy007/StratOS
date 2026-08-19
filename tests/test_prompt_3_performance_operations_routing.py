from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def skill(skill_id: str) -> str:
    return (REPO_ROOT / "global" / "skills" / skill_id / "SKILL.md").read_text(
        encoding="utf-8"
    )


class PromptThreePerformanceOperationsRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.performance = skill("performance")
        cls.operations = skill("devops-infra")
        cls.performance_reference = (
            REPO_ROOT
            / "global"
            / "skills"
            / "performance"
            / "references"
            / "extended-guidance.md"
        ).read_text(encoding="utf-8")
        cls.operations_reference = (
            REPO_ROOT
            / "global"
            / "skills"
            / "devops-infra"
            / "references"
            / "extended-guidance.md"
        ).read_text(encoding="utf-8")

    def test_performance_drops_false_universal_operational_rules(self) -> None:
        self.assertIn("Require p95, p99, production load, profiling, or caching for every task", self.performance)
        self.assertIn("Treat caching as an option, not a last-resort ritual", self.performance)
        self.assertNotIn("Use p95/p99 metrics, never averages", self.performance)
        self.assertNotIn("production-scale data and concurrency", self.performance)

    def test_browser_and_synthetic_evidence_are_labeled_at_the_right_boundary(self) -> None:
        self.assertIn("client or interaction boundary", self.performance)
        self.assertIn("Label evidence as local, synthetic, staging, field, or production", self.performance)
        self.assertIn("Declaring success from server time alone", self.performance_reference)
        self.assertIn("Label synthetic results as synthetic", self.performance_reference)

    def test_cache_and_retry_require_correctness_decisions(self) -> None:
        self.assertIn("freshness and invalidation rule", self.performance)
        self.assertIn("idempotency, deadline, retry-budget", self.performance)
        self.assertIn("Authorization and privacy boundary", self.performance_reference)
        self.assertIn("Retry budget, backoff, and jitter", self.performance_reference)

    def test_operations_uses_proportional_controls_and_actionable_alerts(self) -> None:
        self.assertIn("as universal baselines", self.operations)
        self.assertIn("Select signals by question", self.operations)
        self.assertIn("Page on actionable current or imminent user/business harm", self.operations)
        self.assertIn("Maturity checklist import", self.operations_reference)

    def test_delivery_treats_rollback_as_a_stateful_recovery_question(self) -> None:
        self.assertIn("Treat rollout as a decision point, not proof", self.operations)
        self.assertIn("binary rollback cannot safely restore state", self.operations)
        self.assertIn("external, production, destructive, or financially consequential effect", self.operations_reference)
        self.assertIn("generic rollback may be inadequate", self.operations_reference)

    def test_skills_keep_external_effects_approval_gated(self) -> None:
        self.assertIn("required human approval before effect", self.performance)
        self.assertIn("required just-in-time human approval", self.operations)
        self.assertIn("without the required just-in-time human approval", self.operations)


if __name__ == "__main__":
    unittest.main()
