from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MediaProviderContractTests(unittest.TestCase):
    def read(self, relative_path: str) -> str:
        return (ROOT / relative_path).read_text(encoding="utf-8")

    def test_video_generation_routes_before_provider_syntax(self) -> None:
        skill = self.read("global/skills/video-generation/SKILL.md")
        index = self.read("global/skills/video-generation/references/resource-index.md")

        self.assertIn("concept_test", skill)
        self.assertIn("neutral production brief", skill)
        self.assertIn("active-surface", skill)
        self.assertIn("Load only the reference material required", skill)
        self.assertIn("google-flow.md", index)
        self.assertIn("seedance-routing.md", index)

    def test_google_reference_keeps_aliases_and_extension_conditional(self) -> None:
        reference = self.read("global/skills/video-generation/references/google-flow.md")

        self.assertIn("Google creative interface", reference)
        self.assertIn("Veo 3.1 Flash", reference)
        self.assertIn("unresolved user language", reference)
        self.assertIn("matrix and credit table disagree", reference)
        self.assertIn("visible Extend control", reference)

    def test_seedance_is_a_conditional_reference_inside_the_single_skill(self) -> None:
        skill = self.read("global/skills/video-generation/SKILL.md")
        routing = self.read("global/skills/video-generation/references/seedance-routing.md")

        self.assertIn("seedance-routing.md", skill)
        self.assertIn("not one invariant interface", routing)
        self.assertIn("Seedance 2.0 launch", routing)
        self.assertIn("Seedance 2.5 launch", routing)
        self.assertIn("Do not infer price, quality, or access", routing)
        self.assertFalse((ROOT / "global/skills/seedance").exists())


if __name__ == "__main__":
    unittest.main()
