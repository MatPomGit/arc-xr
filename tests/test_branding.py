"""Approved ARC-XR logo in isolated Pages, with text-only fallback."""
from __future__ import annotations
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from site_branding import expected_config
from validate_pages import check_pages


class BrandingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "xr"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(
            ".git", ".venv", "__pycache__", "site"))

    def tearDown(self):
        self.tmp.cleanup()

    def test_without_logo_header_is_textual(self):
        actual = (self.root / "mkdocs.yml").read_text()
        expected, logo = expected_config(self.root)
        self.assertIsNone(logo)
        self.assertEqual(actual, expected)
        self.assertEqual([], check_pages(self.root))

    def test_hash_approved_logo_activates_mkdocs_header(self):
        image = self.root / "pages/assets/brand/logo.png"
        image.parent.mkdir(parents=True)
        image.write_bytes(b"\x89PNG\r\n\x1a\n" + b"reviewed-test-logo")
        policy = self.root / "config/pages-policy.json"
        obj = json.loads(policy.read_text())
        obj["public_files"].append("assets/brand/logo.png")
        obj["approved_image_sha256"]["assets/brand/logo.png"] = hashlib.sha256(
            image.read_bytes()).hexdigest()
        policy.write_text(json.dumps(obj))
        expected, logo = expected_config(self.root)
        self.assertEqual("assets/brand/logo.png", logo)
        (self.root / "mkdocs.yml").write_text(expected)
        self.assertEqual([], check_pages(self.root))

    def test_unapproved_logo_is_rejected(self):
        image = self.root / "pages/assets/brand/logo.png"
        image.parent.mkdir(parents=True)
        image.write_bytes(b"not-reviewed")
        with self.assertRaisesRegex(ValueError, "Unapproved"):
            expected_config(self.root)
        self.assertTrue(any("PAGES LOGO:" in error for error in check_pages(self.root)))


if __name__ == "__main__":
    unittest.main()
