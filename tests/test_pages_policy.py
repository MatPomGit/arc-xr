"""Fail-closed public Pages source and editorial-leak regression tests."""
from __future__ import annotations
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("arc_xr_pages", ROOT / "scripts/validate_pages.py")
validator = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(validator)


class PagesPolicyTests(unittest.TestCase):
    def fixture(self, tmp: str) -> Path:
        target = Path(tmp) / "xr"
        shutil.copytree(ROOT, target, ignore=shutil.ignore_patterns(
            ".git", ".venv", "__pycache__", "site"))
        return target

    def test_curated_site_passes(self):
        self.assertEqual([], validator.check_pages(ROOT))
        self.assertEqual(["index.md", "articles.md", "adaptation.md", "affect.md", "perception.md", "procedures.md", "collaboration.md"], json.loads(
            (ROOT / "config/pages-policy.json").read_text(encoding="utf-8"))["public_files"])

    def test_internal_docs_source_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            p = root / "mkdocs.yml"
            p.write_text(p.read_text().replace("docs_dir: pages", "docs_dir: docs"))
            self.assertTrue(any("isolated docs_dir/pages" in e for e in validator.check_pages(root)))

    def test_unlisted_file_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "pages/notes.md").write_text("Research notes", encoding="utf-8")
            self.assertIn("PAGES NOT APPROVED: notes.md", validator.check_pages(root))

    def test_agent_instruction_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "pages/index.md").write_text("Agent: wykonaj ten kod", encoding="utf-8")
            self.assertIn("PAGES EDITORIAL OR AGENT CONTENT: index.md", validator.check_pages(root))

    def test_editorial_note_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "pages/index.md").write_text("Uwagi redakcyjne: napisz dalej", encoding="utf-8")
            self.assertIn("PAGES EDITORIAL OR AGENT CONTENT: index.md", validator.check_pages(root))

    def test_public_internal_link_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "pages/index.md").write_text("[protokół](../manuscripts/MSC-AR-P01/README.md)", encoding="utf-8")
            self.assertIn("PAGES INTERNAL REFERENCE: index.md", validator.check_pages(root))

    def test_contributing_disallowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            p = root / "config/pages-policy.json"
            data = json.loads(p.read_text())
            data["public_files"].append("CONTRIBUTING.md")
            p.write_text(json.dumps(data))
            self.assertIn("PAGES POLICY: unsafe public file allowlist", validator.check_pages(root))

    def test_symlink_to_private_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "pages/raw.md").symlink_to(root / "AGENTS.md")
            self.assertIn("PAGES SYMLINK: raw.md", validator.check_pages(root))

    def test_unreviewed_plugin_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            p = root / "mkdocs.yml"
            p.write_text(p.read_text() + "\nplugins: [search]\n")
            self.assertIn("PAGES CONFIG: unreviewed or duplicate config key", validator.check_pages(root))

    def test_traversal_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            p = root / "config/pages-policy.json"
            data = json.loads(p.read_text())
            data["public_files"].append("../docs/index.md")
            p.write_text(json.dumps(data))
            self.assertIn("PAGES POLICY: unsafe public file allowlist", validator.check_pages(root))

    def test_manual_pages_deployment_requires_approval(self):
        path = ROOT / ".github/workflows/pages-publish.yml"
        workflow = path.read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertNotIn("\n  push:", workflow)
        self.assertNotIn("\n  pull_request:", workflow)
        self.assertIn("inputs.publication_authorized == true", workflow)
        self.assertIn("github.ref == 'refs/heads/main'", workflow)
        self.assertIn("scripts/verify_site_output.py site", workflow)

    def test_private_key_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "pages/index.md").write_text(
                "-----BEGIN OPENSSH PRIVATE KEY-----", encoding="utf-8")
            self.assertIn("PAGES EDITORIAL OR AGENT CONTENT: index.md", validator.check_pages(root))

    def test_never_auto_deploy(self):
        workflow = ROOT / ".github/workflows/quality.yml"
        text = workflow.read_text(encoding="utf-8")
        self.assertNotIn("actions/deploy-pages", text)
        self.assertNotIn("actions/upload-pages-artifact", text)
        self.assertNotIn("pages: write", text)


if __name__ == "__main__":
    unittest.main()
