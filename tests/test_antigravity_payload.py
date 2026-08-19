from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "global" / "scripts" / "os.py"


def load_os_module():
    spec = importlib.util.spec_from_file_location("antigravity_os_cli_payload", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load Anti-Gravity OS CLI")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AntigravityPayloadTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()

    def test_all_profiles_generate_discoverable_antigravity_payloads(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output_root = Path(directory)
            payloads = {
                profile: self.os_cli.build_payload(
                    host="antigravity",
                    profile=profile,
                    repo_root=REPO_ROOT,
                    output_root=output_root,
                )
                for profile in ("general", "spatial", "media", "growth")
            }
            for profile, payload in payloads.items():
                self.assertTrue((payload / "GEMINI.md").exists())
                agents = list((payload / ".agents" / "agents").glob("*/agent.md"))
                self.assertEqual(6, len(agents), profile)
                self.assertTrue(
                    (payload / ".agents" / "global_templates" / "decision-evidence-record.md").exists()
                )
                self.assertFalse((payload / ".agents" / "skills" / "deriv-bot-engineering").exists())

            general_skills = payloads["general"] / ".agents" / "skills"
            spatial_skills = payloads["spatial"] / ".agents" / "skills"
            media_skills = payloads["media"] / ".agents" / "skills"
            growth_skills = payloads["growth"] / ".agents" / "skills"
            self.assertFalse((general_skills / "motion-library").exists())
            self.assertFalse((general_skills / "video-generation").exists())
            self.assertTrue((spatial_skills / "motion-library").exists())
            self.assertTrue((media_skills / "video-generation").exists())
            self.assertTrue((growth_skills / "sales-enablement").exists())

    def test_generated_agent_contains_return_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            payload = self.os_cli.build_payload(
                host="antigravity",
                profile="general",
                repo_root=REPO_ROOT,
                output_root=Path(directory),
            )
            rendered = (
                payload / ".agents" / "agents" / "studio-director" / "agent.md"
            ).read_text(encoding="utf-8")
            self.assertIn("## Required specialist return", rendered)
            self.assertIn("## Delegation contract", rendered)


if __name__ == "__main__":
    unittest.main()
