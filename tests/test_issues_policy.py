"""GitHub Issues/JUMP contract regression tests, fully offline."""
from __future__ import annotations
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("xr_issues", ROOT / "scripts/validate_issues.py")
validator = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(validator)


class IssuesTests(unittest.TestCase):
    def fixture(self, tmp: str) -> Path:
        dest = Path(tmp) / "xr"
        shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns(".git", "__pycache__", "site", ".venv"))
        return dest

    def test_new_issue_forms_pass(self):
        self.assertEqual([], validator.check_issues(ROOT))

    def test_generic_task_does_not_force_intent(self):
        self.assertNotIn("\ntitle:", (ROOT / ".github/ISSUE_TEMPLATE/01-task.yml").read_text())

    def test_required_fields_in_all_forms(self):
        for name in validator.EXPECTED:
            content = (ROOT / ".github/ISSUE_TEMPLATE" / name).read_text()
            for field in ("classification", "relations", "acceptance", "verification", "gates", "next_step"):
                with self.subTest(form=name, field=field):
                    self.assertIn("id: " + field, content)

    def test_missing_research_form_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / ".github/ISSUE_TEMPLATE/03-experiment.yml").unlink()
            self.assertIn("ISSUES FORM: missing or unsafe 03-experiment.yml", validator.check_issues(root))

    def test_auto_label_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            path = root / ".github/ISSUE_TEMPLATE/01-task.yml"
            path.write_text(path.read_text() + "\nlabels: [status:ready-for-agent]\n")
            self.assertIn("ISSUES FORM: automatic metadata is not authorized 01-task.yml", validator.check_issues(root))

    def test_required_acceptance_not_optional(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            path = root / ".github/ISSUE_TEMPLATE/02-bug.yml"
            text = path.read_text()
            start = text.index("    id: acceptance")
            pos = text.index("      required: true", start)
            path.write_text(text[:pos] + "      required: false" + text[pos + len("      required: true"):])
            self.assertIn("ISSUES FORM: required field absent or optional 02-bug.yml/acceptance",
                          validator.check_issues(root))

    def test_noncanonical_intent_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            path = root / ".github/ISSUE_TEMPLATE/04-manuscript.yml"
            path.write_text(path.read_text().replace("[paper]", "[task]"))
            self.assertIn("ISSUES FORM: invalid task intent 04-manuscript.yml", validator.check_issues(root))

    def test_unauthorized_dispatch_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            path = root / "config/issues-policy.json"
            data = json.loads(path.read_text())
            data["enable_agent_dispatch"] = True
            path.write_text(json.dumps(data))
            self.assertIn("ISSUES POLICY: labels and dispatch must stay disabled", validator.check_issues(root))

    def test_blank_issue_enabling_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            path = root / ".github/ISSUE_TEMPLATE/config.yml"
            path.write_text(path.read_text().replace("blank_issues_enabled: false", "blank_issues_enabled: true"))
            self.assertIn("ISSUES CONFIG: blank issues must remain disabled", validator.check_issues(root))

    def test_duplicate_field_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            path = root / ".github/ISSUE_TEMPLATE/01-task.yml"
            path.write_text(path.read_text() + "  - type: textarea\n    id: outcome\n    attributes:\n      label: duplicate\n")
            self.assertIn("ISSUES FORM: duplicate field id 01-task.yml", validator.check_issues(root))

    def test_rogue_form_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / ".github/ISSUE_TEMPLATE/05-rogue.yml").write_text("name: other\n")
            self.assertIn("ISSUES UNREVIEWED FORM: 05-rogue.yml", validator.check_issues(root))

    def test_source_not_published_to_pages(self):
        self.assertFalse((ROOT / "pages/issues.md").exists())
        self.assertIn("<!-- agent-work-classification:v1 -->", (ROOT / "docs/issues.md").read_text())


if __name__ == "__main__":
    unittest.main()
