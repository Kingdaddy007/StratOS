from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SpatialOutreachSiteSprintPayloadTests(unittest.TestCase):
    """Retain the older checkout's public profile-scoping regression coverage."""

    @classmethod
    def setUpClass(cls) -> None:
        spec = importlib.util.spec_from_file_location(
            "spatial_outreach_sprint_os", ROOT / "global/scripts/os.py"
        )
        assert spec is not None and spec.loader is not None
        cls.os_cli = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.os_cli)

    def assert_profile_scoping(self, host: str) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            general = self.os_cli.build_payload(
                host=host, repo_root=ROOT, output_root=output
            )
            spatial = self.os_cli.build_payload(
                host=host, profile="spatial", repo_root=ROOT, output_root=output
            )
            relative = Path(".agents/skills/spatial-outreach-site-sprint")
            self.assertFalse((general / relative).exists())
            source = ROOT / "global/skills/spatial-outreach-site-sprint"
            for leaf in (
                Path("SKILL.md"),
                Path("agents/openai.yaml"),
                Path("references/one-shot-prompt-and-intake.md"),
                Path("references/media-production-mode.md"),
            ):
                with self.subTest(resource=leaf):
                    self.assertEqual(
                        (source / leaf).read_bytes(),
                        (spatial / relative / leaf).read_bytes(),
                    )

    def test_codex_profile_exclusion_and_complete_spatial_package(self) -> None:
        self.assert_profile_scoping("codex")

    def test_antigravity_profile_exclusion_and_complete_spatial_package(self) -> None:
        self.assert_profile_scoping("antigravity")


if __name__ == "__main__":
    unittest.main()
