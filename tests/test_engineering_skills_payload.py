from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_IDS = (
    "pr", "retro", "implement-spec", "tdd", "code-review", "writing-for-agents"
)


class EngineeringSkillsPayloadTests(unittest.TestCase):
    """Exercise the public build and installation surfaces with temporary homes."""

    @classmethod
    def setUpClass(cls) -> None:
        spec = importlib.util.spec_from_file_location(
            "engineering_skills_os_cli", REPO_ROOT / "global/scripts/os.py"
        )
        assert spec is not None and spec.loader is not None
        cls.os_cli = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.os_cli)
        cls.temp = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temp.name)
        cls.payloads = {
            host: cls.os_cli.build_payload(
                host, repo_root=REPO_ROOT, output_root=cls.root / "payloads"
            )
            for host in ("codex", "antigravity")
        }

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temp.cleanup()

    def assert_complete_packages(self, skill_root: Path) -> None:
        for skill_id in SKILL_IDS:
            with self.subTest(skill=skill_id):
                source = REPO_ROOT / "global/skills" / skill_id
                installed = skill_root / skill_id
                source_files = {
                    path.relative_to(source) for path in source.rglob("*") if path.is_file()
                }
                installed_files = {
                    path.relative_to(installed)
                    for path in installed.rglob("*") if path.is_file()
                }
                self.assertEqual(source_files, installed_files)
                for relative in source_files:
                    self.assertEqual(
                        (source / relative).read_bytes(),
                        (installed / relative).read_bytes(),
                        str(relative),
                    )

    def test_general_payloads_include_complete_adapted_packages(self) -> None:
        for host, payload in self.payloads.items():
            with self.subTest(host=host):
                self.assert_complete_packages(payload / ".agents/skills")

    def test_codex_invocation_metadata_survives_the_build(self) -> None:
        skills = self.payloads["codex"] / ".agents/skills"
        for skill_id in ("retro", "implement-spec"):
            with self.subTest(skill=skill_id):
                metadata = (skills / skill_id / "agents/openai.yaml").read_text(
                    encoding="utf-8"
                )
                self.assertIn("allow_implicit_invocation: false", metadata)
                self.assertIn(f"${skill_id}", metadata)

    def test_codex_install_discovers_skills_and_preserves_unrelated_state(self) -> None:
        target = self.root / "codex-home"
        sentinel = target / "skills/unrelated/SKILL.md"
        sentinel.parent.mkdir(parents=True)
        sentinel.write_text("unrelated skill\n", encoding="utf-8")
        config = target / "config.toml"
        config.write_text("# user configuration\n", encoding="utf-8")
        self.os_cli.install_codex_global(
            self.payloads["codex"], target, dry_run=False, assume_yes=True
        )
        self.assert_complete_packages(target / "skills")
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "unrelated skill\n")
        self.assertEqual(config.read_text(encoding="utf-8"), "# user configuration\n")
        record = json.loads((target / "antigravity/installation.json").read_text())
        for skill_id in SKILL_IDS:
            self.assertIn(f"skills/{skill_id}", [p.replace("\\", "/") for p in record["direct_targets"]])

    def test_antigravity_install_discovers_skills_and_preserves_unrelated_state(self) -> None:
        target = self.root / ".gemini"
        sentinel = target / "config/skills/unrelated/SKILL.md"
        sentinel.parent.mkdir(parents=True)
        sentinel.write_text("unrelated skill\n", encoding="utf-8")
        config = target / "settings.json"
        config.write_text('{"user_setting": true}\n', encoding="utf-8")
        self.os_cli.install_antigravity_global(
            self.payloads["antigravity"], target, dry_run=False, assume_yes=True
        )
        self.assert_complete_packages(target / "config/skills")
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "unrelated skill\n")
        self.assertEqual(config.read_text(encoding="utf-8"), '{"user_setting": true}\n')


if __name__ == "__main__":
    unittest.main()
