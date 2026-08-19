from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class WorkflowSurvivalAuditTests(unittest.TestCase):
    def test_audit_covers_every_live_manifest_workflow(self) -> None:
        manifest = json.loads(
            (REPO_ROOT / "global" / "manifest.yaml").read_text(encoding="utf-8")
        )
        audit = (
            REPO_ROOT / "docs" / "v4-workflow-survival-audit.md"
        ).read_text(encoding="utf-8")
        workflow_ids = {entry["id"] for entry in manifest["workflows"]}
        for workflow_id in workflow_ids:
            self.assertIn(f"`{workflow_id}`", audit)
        self.assertEqual(17, len(workflow_ids))

    def test_audit_names_demotions_without_claiming_source_deletion(self) -> None:
        audit = (
            REPO_ROOT / "docs" / "v4-workflow-survival-audit.md"
        ).read_text(encoding="utf-8")
        for workflow_id in ("design-ui", "task-dispatch", "test-strategy", "verify-project"):
            self.assertIn(f"| `{workflow_id}` |", audit)
            self.assertIn("Demote candidate", audit)
        self.assertIn("no safe basis for deleting a workflow", audit)


if __name__ == "__main__":
    unittest.main()
