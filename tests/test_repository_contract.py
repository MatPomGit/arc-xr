"""ARC-XR planned programme structure and new governance link consistency."""
from __future__ import annotations
import importlib.util
import re
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("arc_xr_repo", ROOT / "scripts/validate_repository.py")
validator = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(validator)

NEW_DOCS = [
    "AGENTS.md", "ARCHITECTURE.md", "SECURITY.md", "CODE_OF_CONDUCT.md",
    "GOVERNANCE.md", "SUPPORT.md", "README.md", ".github/AGENT_WORKFLOW.md",
    "docs/index.md", "docs/documentation.md", "docs/pages.md",
    "docs/architecture/README.md", "docs/architecture/components.md",
    "docs/architecture/data-flow.md", "docs/architecture/measurement-boundaries.md",
    "docs/security/threat-model.md", "docs/security/incident-response.md",
    "docs/operations/runbook.md", "docs/adr/README.md",
    "docs/adr/0001-programme-boundaries.md",
    "docs/adr/0002-research-and-device-safety.md",
    "docs/adr/0003-public-pages-boundary.md",
]


class RepositoryContractTests(unittest.TestCase):
    def fixture(self, tmp: str) -> Path:
        dest = Path(tmp) / "xr"
        shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns(
            ".git", ".venv", "__pycache__", "build"))
        return dest

    def test_research_contract_passes(self):
        self.assertEqual([], validator.check_repository(ROOT))

    def test_all_six_core_manuscripts_remain(self):
        text = (ROOT / "PROJECT_STATE.yaml").read_text(encoding="utf-8")
        self.assertEqual((
            ["P01", "P02", "P03", "P04", "P05", "P06"], 6),
            validator.state_ids(text))
        for n in range(1, 7):
            self.assertTrue((ROOT / f"manuscripts/MSC-AR-P{n:02}/protocol/README.md").is_file())

    def test_only_one_canonical_article_registry(self):
        self.assertTrue((ROOT / "migration/provenance/papers-v2.json").is_file())
        self.assertFalse((ROOT / "migration/provenance/manuscript_register.md").exists())
        self.assertFalse((ROOT / "migration/provenance/publication_register.md").exists())
        self.assertFalse((ROOT / "manuscripts/source_manifest.json").exists())
        self.assertTrue((ROOT / "migration/provenance/source-manifest-v1.json").is_file())
        self.assertFalse((ROOT / "CONTRIBUTING.md").exists())

    def test_missing_protocol_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "manuscripts/MSC-AR-P03/protocol/README.md").unlink()
            self.assertIn("ARC MANUSCRIPT: missing P03/protocol/README.md",
                          validator.check_repository(root))

    def test_state_count_mismatch_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            p = root / "PROJECT_STATE.yaml"
            p.write_text(p.read_text().replace("planned_core_count: 6", "planned_core_count: 7"))
            self.assertIn("ARC STATE: planned publication count or IDs inconsistent",
                          validator.check_repository(root))

    def test_missing_policy_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "config/pages-policy.json").unlink()
            self.assertTrue(any("PAGES POLICY:" in s for s in validator.check_repository(root)))

    def test_governance_document_links_resolve(self):
        for rel in NEW_DOCS:
            file = ROOT / rel
            source = file.read_text(encoding="utf-8")
            for ref in re.findall(r"\]\(([^)\s]+)\)", source):
                link = ref.split("#", 1)[0].split("?", 1)[0]
                if not link or "://" in link or link.startswith(
                        ("mailto:", "/", "#")):
                    continue
                target = file.parent / link
                with self.subTest(source=rel, target=link):
                    self.assertTrue(target.is_file(), f"Broken link {rel} -> {link}")


if __name__ == "__main__":
    unittest.main()
