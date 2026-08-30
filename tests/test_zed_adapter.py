from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "global" / "scripts" / "os.py"


def load_os_module():
    spec = importlib.util.spec_from_file_location("antigravity_os_cli_zed", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load Anti-Gravity OS CLI")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ZedAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.os_cli = load_os_module()

    def build_payload(self, root: Path) -> Path:
        return self.os_cli.build_payload(
            host="zed",
            profile="general",
            repo_root=REPO_ROOT,
            output_root=root / "build",
        )

    @staticmethod
    def make_directory_link(link: Path, target: Path) -> None:
        try:
            link.symlink_to(target, target_is_directory=True)
            return
        except OSError:
            if os.name != "nt":
                raise
        completed = subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(link), str(target)],
            check=False,
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            raise unittest.SkipTest("directory links are unavailable on this Windows host")

    @staticmethod
    def remove_directory_link(link: Path) -> None:
        if link.is_symlink():
            link.unlink()
        elif link.exists():
            os.rmdir(link)

    def test_zed_payload_labels_roles_as_references(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            payload = self.build_payload(Path(directory))
            self.assertTrue((payload / "AGENTS.md").exists())
            self.assertIn(
                "does not turn Markdown role contracts into selectable custom agents",
                (payload / "AGENTS.md").read_text(encoding="utf-8"),
            )
            self.assertEqual(6, len(list((payload / "agent-contracts").glob("*.md"))))
            self.assertFalse((payload / "prompts").exists())
            self.assertTrue((payload / "workflows" / "workflow-task-dispatch.md").exists())
            support_skill = payload / "skills" / "antigravity-v4"
            self.assertTrue((support_skill / "SKILL.md").exists())
            self.assertTrue((support_skill / "references" / "GLOBAL_MEMORY.md").exists())
            self.assertTrue(
                (support_skill / "references" / "workflows" / "workflow-task-dispatch.md").exists()
            )
            self.assertTrue(
                (support_skill / "references" / "agent-contracts" / "studio-director.md").exists()
            )
            adapter = json.loads((payload / "adapter.json").read_text(encoding="utf-8"))
            self.assertTrue(adapter["supports_slash_commands"])
            self.assertFalse(adapter["native_custom_agents"])
            self.assertIn("invoke_agent", adapter["capabilities"])

    def test_zed_global_install_merges_policy_and_preserves_unrelated_skill(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = self.build_payload(root)
            zed_home = root / "Zed"
            zed_home.mkdir()
            (zed_home / "AGENTS.md").write_text("User-authored Zed instructions\n", encoding="utf-8")
            skills_root = root / "home" / ".agents" / "skills"
            unrelated = skills_root / "unrelated"
            unrelated.mkdir(parents=True)
            (unrelated / "SKILL.md").write_text("keep me\n", encoding="utf-8")

            preview = self.os_cli.install_zed_global(
                payload, zed_home, True, False, skills_root=skills_root
            )
            self.assertEqual("dry-run", preview["status"])
            self.assertEqual("User-authored Zed instructions\n", (zed_home / "AGENTS.md").read_text())
            self.assertFalse((zed_home / "GLOBAL_MEMORY.md").exists())
            self.assertTrue(
                all(
                    target.startswith("antigravity/") or target == "AGENTS.md" or target.startswith("skills/")
                    for target in preview["changes"]["add"]
                )
            )

            result = self.os_cli.install_zed_global(
                payload, zed_home, False, True, skills_root=skills_root
            )
            self.assertEqual("installed", result["status"])
            policy = (zed_home / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("User-authored Zed instructions", policy)
            self.assertIn(self.os_cli.ZED_MANAGED_START, policy)
            self.assertIn("Zed's native Agent", policy)
            self.assertTrue((zed_home / "antigravity" / "GLOBAL_MEMORY.md").exists())
            self.assertTrue(
                (zed_home / "antigravity" / "workflows" / "workflow-task-dispatch.md").exists()
            )
            self.assertTrue(
                (zed_home / "antigravity" / "agent-contracts" / "studio-director.md").exists()
            )
            self.assertTrue((skills_root / "coding" / "SKILL.md").exists())
            self.assertTrue((skills_root / "antigravity-v4" / "SKILL.md").exists())
            self.assertTrue(
                (
                    skills_root
                    / "antigravity-v4"
                    / "references"
                    / "GLOBAL_MEMORY.md"
                ).exists()
            )
            self.assertEqual("keep me\n", (unrelated / "SKILL.md").read_text(encoding="utf-8"))
            self.assertTrue((zed_home / "antigravity" / "installation.json").exists())
            self.assertFalse((zed_home / "GLOBAL_MEMORY.md").exists())
            self.assertFalse((zed_home / "workflows").exists())
            self.assertFalse((zed_home / "agent-contracts").exists())
            self.assertFalse((zed_home / "core").exists())
            self.assertFalse((zed_home / "memory").exists())
            self.assertFalse((zed_home / "schemas").exists())
            self.assertEqual(
                str(skills_root / "antigravity-v4"),
                result["direct_discovery"]["runtime_support_skill"],
            )

            repeat = self.os_cli.install_zed_global(
                payload, zed_home, False, True, skills_root=skills_root
            )
            self.assertEqual("installed", repeat["status"])
            self.assertEqual(policy, (zed_home / "AGENTS.md").read_text(encoding="utf-8"))

    def test_zed_global_install_creates_missing_config_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = self.build_payload(root)
            zed_home = root / "Zed"
            skills_root = root / "home" / ".agents" / "skills"
            result = self.os_cli.install_zed_global(
                payload, zed_home, False, True, skills_root=skills_root
            )
            self.assertEqual("installed", result["status"])
            self.assertTrue((zed_home / "AGENTS.md").exists())
            self.assertTrue((skills_root / "coding" / "SKILL.md").exists())

    def test_zed_workspace_install_uses_project_discovery_and_merges_policy(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = self.build_payload(root)
            workspace = root / "project"
            workspace.mkdir()
            (workspace / "AGENTS.md").write_text("Project instructions\n", encoding="utf-8")
            unrelated = workspace / ".agents" / "skills" / "unrelated"
            unrelated.mkdir(parents=True)
            (unrelated / "SKILL.md").write_text("keep me\n", encoding="utf-8")

            preview = self.os_cli.install_zed_workspace(payload, workspace, True, False)
            self.assertEqual("dry-run", preview["status"])
            self.assertFalse((workspace / ".agents" / "GLOBAL_MEMORY.md").exists())

            result = self.os_cli.install_zed_workspace(payload, workspace, False, True)
            self.assertEqual("installed", result["status"])
            policy = (workspace / "AGENTS.md").read_text(encoding="utf-8")
            self.assertIn("Project instructions", policy)
            self.assertIn(self.os_cli.ZED_MANAGED_START, policy)
            self.assertTrue((workspace / ".agents" / "antigravity" / "GLOBAL_MEMORY.md").exists())
            self.assertTrue((workspace / ".agents" / "skills" / "coding" / "SKILL.md").exists())
            self.assertTrue(
                (workspace / ".agents" / "skills" / "antigravity-v4" / "SKILL.md").exists()
            )
            self.assertTrue(
                (
                    workspace
                    / ".agents"
                    / "antigravity"
                    / "workflows"
                    / "workflow-verify-project.md"
                ).exists()
            )
            self.assertTrue(
                (
                    workspace
                    / ".agents"
                    / "antigravity"
                    / "agent-contracts"
                    / "design-director.md"
                ).exists()
            )
            self.assertTrue((workspace / ".agents" / "antigravity" / "installation.json").exists())
            self.assertFalse((workspace / ".agents" / "GLOBAL_MEMORY.md").exists())
            self.assertFalse((workspace / ".agents" / "workflows").exists())
            self.assertFalse((workspace / ".agents" / "agent-contracts").exists())
            self.assertEqual("keep me\n", (unrelated / "SKILL.md").read_text(encoding="utf-8"))

    def test_zed_install_refuses_unmanaged_skill_collision(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = self.build_payload(root)
            workspace = root / "project"
            workspace.mkdir()
            conflicting = workspace / ".agents" / "skills" / "coding"
            conflicting.mkdir(parents=True)
            (conflicting / "SKILL.md").write_text("user-owned\n", encoding="utf-8")
            with self.assertRaises(self.os_cli.InstallationRefused):
                self.os_cli.install_zed_workspace(payload, workspace, True, False)

    def test_zed_global_install_refuses_reparse_point_parent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = self.build_payload(root)
            zed_home = root / "Zed"
            zed_home.mkdir()
            redirected = root / "redirected"
            redirected.mkdir()
            sentinel = redirected / "sentinel.txt"
            sentinel.write_text("must survive\n", encoding="utf-8")
            linked_namespace = zed_home / "antigravity"
            self.make_directory_link(linked_namespace, redirected)
            try:
                with self.assertRaisesRegex(self.os_cli.InstallationRefused, "symlink|reparse-point"):
                    self.os_cli.install_zed_global(
                        payload, zed_home, True, False, skills_root=root / "home" / ".agents" / "skills"
                    )
                self.assertEqual("must survive\n", sentinel.read_text(encoding="utf-8"))
            finally:
                self.remove_directory_link(linked_namespace)

    def test_zed_workspace_install_refuses_higher_priority_instruction_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = self.build_payload(root)
            workspace = root / "project"
            workspace.mkdir()
            (workspace / ".cursorrules").write_text("legacy instructions\n", encoding="utf-8")
            with self.assertRaisesRegex(self.os_cli.InstallationRefused, "higher-priority"):
                self.os_cli.install_zed_workspace(payload, workspace, True, False)

    def test_zed_cli_requires_explicit_native_install_mode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "Zed"
            result = self.os_cli.main(
                [
                    "install",
                    "--host",
                    "zed",
                    "--target",
                    str(target),
                    "--option",
                    "general",
                    "--dry-run",
                ]
            )
            self.assertEqual(2, result)
            self.assertFalse(target.exists())

    def test_zed_policy_rejects_malformed_managed_markers(self) -> None:
        malformed = (
            f"{self.os_cli.ZED_MANAGED_START}\n"
            f"{self.os_cli.ZED_MANAGED_START}\n"
            f"{self.os_cli.ZED_MANAGED_END}\n"
        )
        with self.assertRaises(self.os_cli.InstallationRefused):
            self.os_cli.merge_zed_policy(malformed, "new policy")


if __name__ == "__main__":
    unittest.main()
