from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GLOBAL = ROOT / "global"
SKILLS = (
    "spatial-experience-design",
    "storytelling",
    "cinematic-motion",
    "media-choreography",
    "master-design-director",
)


def load_os_module():
    spec = importlib.util.spec_from_file_location("v5_spatial_os", GLOBAL / "scripts" / "os.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("OS CLI unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class V5SpatialIntegrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manifest = json.loads((GLOBAL / "manifest.yaml").read_text(encoding="utf-8"))
        self.os_cli = load_os_module()

    def test_registry_and_legacy_route_are_coherent(self) -> None:
        registered = {record["id"] for record in self.manifest["skills"]}
        self.assertTrue(set(SKILLS + ("spatial-outreach-site-sprint",)).issubset(registered))
        constitution = GLOBAL / "reference" / "v5-creative-constitution-v1.0.0.md"
        self.assertIn("v1.0.0", constitution.read_text(encoding="utf-8").splitlines()[0])
        resources = {record["id"] for record in self.manifest["resources"]}
        self.assertIn("v5-creative-constitution-v1.0.0", resources)
        workflows = [record for record in self.manifest["workflows"] if record["id"] == "spatial-project-inception"]
        self.assertEqual(1, len(workflows))
        metadata, _ = self.os_cli.split_frontmatter(GLOBAL / "workflows" / "workflow-spatial-project-inception.md")
        self.assertEqual("active", metadata["status"])
        self.assertIsInstance(metadata["version"], int)
        legacy = (GLOBAL / "skills" / "cinematic-showroom-strategy" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("load `media-choreography`", legacy)
        director, _ = self.os_cli.split_frontmatter(GLOBAL / "agents" / "design-director" / "AGENT.md")
        spatial = next(item["skills"] for item in director["conditional_skills"] if "spatial" in item["profiles"])
        self.assertIn("media-choreography", spatial)
        self.assertNotIn("cinematic-showroom-strategy", spatial)

    def test_spatial_resources_are_discoverable_in_both_active_host_payloads(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            for host in ("codex", "antigravity"):
                payload = self.os_cli.build_payload(
                    host=host,
                    profile="spatial",
                    repo_root=ROOT,
                    output_root=Path(directory) / host,
                )
                self.assertTrue((payload / ("AGENTS.md" if host == "codex" else "GEMINI.md")).is_file())
                content = payload / ".agents"
                self.assertTrue((content / "reference" / "v5-creative-constitution-v1.0.0.md").is_file())
                self.assertEqual(
                    1,
                    len(list((content / "workflows").glob("workflow-spatial-project-inception*.md"))),
                )
                for name in SKILLS:
                    self.assertTrue((content / "skills" / name / "SKILL.md").is_file(), (host, name))
                    self.assertTrue(list((content / "skills" / name / "references").glob("*.md")), (host, name))
                self.assertTrue((content / "skills" / "spatial-outreach-site-sprint" / "SKILL.md").is_file())

    def test_contrasting_routes_preserve_general_boundary(self) -> None:
        fixture = json.loads((ROOT / "tests" / "fixtures" / "routing.json").read_text(encoding="utf-8"))
        scenarios = {item["id"]: item for item in fixture["scenarios"]}
        self.assertEqual("reference-intelligence", scenarios["spatial-reference-analysis"]["route"])
        self.assertEqual("spatial-project-inception", scenarios["spatial-portfolio-inception"]["route"])
        self.assertEqual("media-choreography", scenarios["v5-spatial-media-feasibility"]["route"])
        self.assertEqual([], scenarios["v5-ordinary-product-framing"]["active_packs"])
        self.assertEqual("product-thinking", scenarios["v5-ordinary-product-framing"]["route"])
        with tempfile.TemporaryDirectory() as directory:
            payload = self.os_cli.build_payload(
                host="codex",
                profile="general",
                repo_root=ROOT,
                output_root=Path(directory),
            )
            self.assertFalse((payload / ".agents" / "skills" / "media-choreography").exists())
            self.assertFalse((payload / ".agents" / "reference" / "v5-creative-constitution-v1.0.0.md").exists())


if __name__ == "__main__":
    unittest.main()
