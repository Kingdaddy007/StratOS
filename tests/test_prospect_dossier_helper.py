from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
HELPER_PATH = (
    REPO_ROOT
    / "global"
    / "skills"
    / "prospect-research"
    / "scripts"
    / "dossier_helper.py"
)


def load_helper_module():
    spec = importlib.util.spec_from_file_location("prospect_dossier_helper", HELPER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load prospect dossier helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProspectDossierHelperTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.helper = load_helper_module()

    def valid_dossier(self) -> dict:
        dossier = self.helper.new_dossier()
        dossier.update(
            {
                "studio_name": "Example Studio",
                "country": "Nigeria",
                "city": "Port Harcourt",
                "website_url": "https://example.com",
                "instagram_url": "https://instagram.com/example",
                "founder_name": "Example Founder",
                "contact_method": "public email",
                "website_status": "static portfolio with no named conversion path",
                "inspection_date": "2026-08-19",
                "main_gap": "No inquiry path",
                "outreach_hook": "A public project page has no way to discuss a similar commission",
                "evidence": {
                    "instagram": "Recent completed residence project with public contact information.",
                    "website": "Portfolio has no inquiry path on inspected contact page.",
                    "completed_projects": "Publicly labelled completed residential project.",
                    "premium_positioning": "Public service language identifies bespoke residential design.",
                },
            }
        )
        return dossier

    def test_new_dossier_defaults_to_a_non_external_action(self) -> None:
        dossier = self.helper.new_dossier()

        self.assertEqual("Verify manually", dossier["recommended_action"])
        self.assertIn("Verify manually", self.helper.ALLOWED_RECOMMENDED_ACTIONS)
        self.assertNotIn("Send light outreach", self.helper.ALLOWED_RECOMMENDED_ACTIONS)

    def test_elite_concept_is_a_review_proposal_not_an_external_action(self) -> None:
        dossier = self.valid_dossier()
        dossier["scores"] = {
            "visual_asset_quality": 25,
            "website_gap": 20,
            "business_maturity": 10,
            "active_online_presence": 15,
            "contact_accessibility": 10,
            "personalization_potential": 10,
        }
        dossier["recommended_action"] = "Prepare concept for review"

        self.assertEqual([], self.helper.validate_dossier(dossier))
        self.assertEqual("Elite", self.helper.score_dossier(dossier)["tier"])

    def test_invalid_or_under_threshold_concept_action_is_rejected(self) -> None:
        dossier = self.valid_dossier()
        dossier["recommended_action"] = "Create concept immediately"

        self.assertTrue(any("recommended_action must be one of" in error for error in self.helper.validate_dossier(dossier)))

        dossier["recommended_action"] = "Prepare concept for review"
        self.assertTrue(any("Elite score" in error for error in self.helper.validate_dossier(dossier)))


if __name__ == "__main__":
    unittest.main()
