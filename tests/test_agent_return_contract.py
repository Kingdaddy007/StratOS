from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "global" / "scripts" / "os.py"


def load_os_module():
    spec = importlib.util.spec_from_file_location("antigravity_os_cli_agent_contract", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load Anti-Gravity OS CLI")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AgentReturnContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()

    def test_every_canonical_agent_declares_evidence_return_and_delegation_contract(self) -> None:
        problems, agents = self.os_cli.validate_agent_files(REPO_ROOT)
        self.assertEqual([], problems)
        self.assertEqual(6, len(agents))
        for metadata in agents.values():
            self.assertGreaterEqual(len(metadata["return_contract"]), 4)
            self.assertGreaterEqual(len(metadata["delegation_contract"]), 3)
            self.assertTrue(any("owner" in value.lower() for value in metadata["return_contract"]))
            self.assertTrue(any("bounded" in value.lower() for value in metadata["delegation_contract"]))

    def test_every_delegating_agent_has_real_collaboration_capabilities(self) -> None:
        problems, agents = self.os_cli.validate_agent_files(REPO_ROOT)
        self.assertEqual([], problems)
        required = {
            "invoke_agent",
            "define_worker",
            "message_agent",
            "manage_agents",
        }
        for agent_id, metadata in agents.items():
            self.assertTrue(metadata["can_delegate"], agent_id)
            self.assertTrue(
                required.issubset(metadata["tool_capabilities"]),
                f"{agent_id} declares delegation without the full collaboration ceiling",
            )

    def test_validation_rejects_delegation_without_collaboration_tools(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temporary_root = Path(directory)
            target = temporary_root / "global" / "agents"
            shutil.copytree(REPO_ROOT / "global" / "agents", target)
            director = target / "studio-director" / "AGENT.md"
            text = director.read_text(encoding="utf-8")
            text = text.replace(", invoke_agent", "", 1)
            director.write_text(text, encoding="utf-8")

            problems, _ = self.os_cli.validate_agent_files(temporary_root)

            self.assertTrue(
                any(problem["code"] == "agent-delegation-tools" for problem in problems),
                problems,
            )

    def test_schema_requires_the_shared_contract_fields(self) -> None:
        schema = json.loads(
            (REPO_ROOT / "global" / "schemas" / "agent.schema.json").read_text(encoding="utf-8")
        )
        self.assertIn("return_contract", schema["required"])
        self.assertIn("delegation_contract", schema["required"])
        self.assertEqual("array", schema["properties"]["return_contract"]["type"])
        self.assertEqual("array", schema["properties"]["delegation_contract"]["type"])
        tool_values = set(schema["properties"]["tool_capabilities"]["items"]["enum"])
        self.assertTrue(
            {"invoke_agent", "define_worker", "message_agent", "manage_agents"}.issubset(
                tool_values
            )
        )

    def test_generated_antigravity_agents_expose_the_contract(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            payload = self.os_cli.build_payload(
                host="antigravity",
                profile="general",
                repo_root=REPO_ROOT,
                output_root=Path(directory),
            )
            for agent_id in (
                "assurance-quality-lead",
                "design-director",
                "product-strategy-lead",
                "staff-engineer",
                "studio-director",
                "systems-architect",
            ):
                rendered = (
                    payload / ".agents" / "agents" / agent_id / "agent.md"
                ).read_text(encoding="utf-8")
                self.assertIn("## Required specialist return", rendered)
                self.assertIn("## Delegation contract", rendered)
                self.assertIn("  - invoke_subagent", rendered)
                self.assertIn("  - define_subagent", rendered)
                self.assertIn("  - send_message", rendered)
                self.assertIn("  - manage_subagents", rendered)
                self.assertIn("## Host-enabled delegation", rendered)
                self.assertIn("Workers cannot create children", rendered)
                self.assertIn("final independent assurance", rendered)


if __name__ == "__main__":
    unittest.main()
