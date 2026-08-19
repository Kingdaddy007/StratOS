from __future__ import annotations

import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SECURITY_ROOT = REPO_ROOT / "global" / "skills" / "security"


class PromptFourApplicationSecurityRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.security = (SECURITY_ROOT / "SKILL.md").read_text(encoding="utf-8")
        cls.reference = (
            SECURITY_ROOT / "references" / "boundary-evidence-and-review.md"
        ).read_text(encoding="utf-8")
        cls.index = (SECURITY_ROOT / "references" / "resource-index.md").read_text(
            encoding="utf-8"
        )

    def test_activation_is_boundary_triggered_not_implicitly_always_on(self) -> None:
        self.assertIn("trust boundary", self.security)
        self.assertIn("Do not load for a purely local, reversible change", self.security)
        self.assertNotIn("implicitly always active", self.security)

    def test_security_method_requires_boundary_abuse_case_control_and_evidence(self) -> None:
        for expected in (
            "**Boundary.**",
            "**Abuse case.**",
            "**Control.**",
            "**Evidence.**",
            "**Review.**",
            "**Remediate and verify.**",
        ):
            self.assertIn(expected, self.security)
        self.assertIn("actor or source -> action or input -> vulnerable sink or capability", self.security)
        self.assertIn("direct, indirect, synthetic, environment-limited, or missing", self.security)

    def test_authorization_is_server_side_and_negative_path_focused(self) -> None:
        self.assertIn("Enforce authorization at the authoritative server boundary", self.security)
        self.assertIn("cross-user/cross-tenant", self.security)
        self.assertIn("Test identity, object/tenant ownership", self.reference)
        self.assertIn("RBAC, MFA, secret managers", self.reference)

    def test_agent_content_and_tool_actions_remain_untrusted_and_gated(self) -> None:
        self.assertIn("repository text, webpages, documents, logs, tool output, memory", self.security)
        self.assertIn("narrow scopes/destinations", self.security)
        self.assertIn("confirmation for high-impact actions", self.security)
        self.assertIn("attempted tool escalation", self.reference)

    def test_finding_dimensions_and_guarantee_limits_are_explicit(self) -> None:
        self.assertIn("`critical`, `high`, `medium`, or `low`", self.security)
        self.assertIn("confidence", self.security)
        self.assertIn("exploitability", self.security)
        self.assertIn("evidence quality", self.security)
        self.assertIn("never make a security guarantee", self.security)
        self.assertIn("runtime risk decision", self.reference)

    def test_external_and_high_consequence_effects_stay_human_approved(self) -> None:
        self.assertIn("required human approval", self.security)
        self.assertIn("external, identity, access-control", self.security)
        self.assertIn("lacks approval", self.reference)

    def test_dated_references_are_indexed_for_conditional_loading(self) -> None:
        self.assertIn("OWASP ASVS 5.0.0", self.index)
        self.assertIn("NIST SSDF", self.index)
        self.assertIn("OWASP AI Agent Security", self.index)
        self.assertIn("2026-08-19", self.index)


if __name__ == "__main__":
    unittest.main()
