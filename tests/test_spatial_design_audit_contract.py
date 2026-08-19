from __future__ import annotations

import json
import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OS_MODULE_PATH = ROOT / "global" / "scripts" / "os.py"


def load_os_module():
    spec = importlib.util.spec_from_file_location("design_audit_os_cli", OS_MODULE_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load Anti-Gravity OS CLI")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SpatialDesignAuditLibraryContractTests(unittest.TestCase):
    def test_canvas_ui_is_conditional_spatial_capability_with_no_general_leak(self) -> None:
        manifest = json.loads((ROOT / "global" / "manifest.yaml").read_text(encoding="utf-8"))
        record = next(item for item in manifest["skills"] if item["id"] == "canvas-ui")
        skill = (ROOT / record["path"] / "SKILL.md").read_text(encoding="utf-8")
        reference = (
            ROOT
            / record["path"]
            / "references"
            / "component-selection-and-fallbacks.md"
        ).read_text(encoding="utf-8")

        self.assertEqual(["spatial"], record["profiles"])
        self.assertEqual("design_direction", record["functional_owner"])
        self.assertIn("still, DOM/CSS", skill)
        self.assertIn("just-in-time approval", skill)
        self.assertIn("semantic content", skill)
        self.assertIn("Do not use the old host-local", reference)

        os_cli = load_os_module()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            general = os_cli.build_payload(
                host="antigravity",
                profile="general",
                repo_root=ROOT,
                output_root=output,
            )
            spatial = os_cli.build_payload(
                host="antigravity",
                profile="spatial",
                repo_root=ROOT,
                output_root=output,
            )
            self.assertFalse((general / ".agents" / "skills" / "canvas-ui").exists())
            self.assertTrue((spatial / ".agents" / "skills" / "canvas-ui" / "SKILL.md").is_file())
            self.assertTrue(
                (spatial / ".agents" / "skills" / "canvas-ui" / "agents" / "openai.yaml").is_file()
            )

    def test_library_is_complete_spatial_only_and_discoverable(self) -> None:
        design_audit = ROOT / "global" / "design-audit"
        reports = sorted(design_audit.glob("site-*.md"))
        index = (design_audit / "library-index.md").read_text(encoding="utf-8")
        adaptation_map = (
            ROOT
            / "global"
            / "skills"
            / "spatial-experience-design"
            / "reference"
            / "audit-mechanics-map.md"
        ).read_text(encoding="utf-8")
        reference_skill = (
            ROOT / "global" / "skills" / "reference-intelligence" / "SKILL.md"
        ).read_text(encoding="utf-8")
        library_reference = (
            ROOT
            / "global"
            / "skills"
            / "reference-intelligence"
            / "references"
            / "local-design-audit-library.md"
        ).read_text(encoding="utf-8")
        manifest = json.loads((ROOT / "global" / "manifest.yaml").read_text(encoding="utf-8"))

        self.assertEqual(30, len(reports))
        for number in range(1, 31):
            label = f"{number:02d}"
            self.assertIn(f"Site {label}", adaptation_map)
            self.assertIn(f"{label} ", index)

        resource = next(
            item
            for item in manifest["resources"]
            if item["id"] == "spatial-design-audit-library"
        )
        self.assertEqual(["spatial"], resource["profiles"])
        self.assertIn("local-design-audit-library.md", reference_skill)
        self.assertIn("mediated reference notes", library_reference)
        self.assertIn("vision-capable agent", library_reference)
        self.assertIn("not permission to copy", library_reference)

    def test_library_is_in_a_spatial_payload_and_absent_from_general(self) -> None:
        os_cli = load_os_module()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            general = os_cli.build_payload(
                host="gemini",
                profile="general",
                repo_root=ROOT,
                output_root=output,
            )
            spatial = os_cli.build_payload(
                host="gemini",
                profile="spatial",
                repo_root=ROOT,
                output_root=output,
            )

            self.assertFalse((general / "design-audit").exists())
            self.assertTrue((spatial / "design-audit" / "library-index.md").is_file())
            self.assertEqual(30, len(list((spatial / "design-audit").glob("site-*.md"))))


if __name__ == "__main__":
    unittest.main()
