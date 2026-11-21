"""Canonical v2 registry: scientific truth, source integrity, public privacy."""
from __future__ import annotations
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_arc_v2_registry import audit


class ArcV2RegistryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)/"arc"
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns(".git","site","__pycache__"))
    def tearDown(self):
        self.temp.cleanup()
    def load(self,name):
        return json.loads((self.root/name).read_text(encoding="utf-8"))
    def save(self,name,data):
        (self.root/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n")
    def papers(self):
        return self.load("portfolio/papers.json")
    def verify_bad(self,token):
        errors=audit(self.root)
        self.assertTrue(any(token in x for x in errors),errors)

    def test_canonical_migration_passes(self):
        self.assertEqual([],audit(ROOT))
        self.assertEqual([],audit(self.root))

    def test_28_entries_preserve_historical_27_records(self):
        paper=self.papers()["papers"]
        self.assertEqual(len(paper),28)
        self.assertEqual(len({p["id"] for p in paper}),28)
        self.assertEqual(sum(p["owner"]["mode"]=="local" for p in paper),27)
        self.assertEqual(sum(p["owner"]["redacted"] is True for p in paper
                             if p["owner"]["mode"]=="external"),1)
        self.assertEqual(sum(p["publication_stage"]=="draft" for p in paper),7)
        self.assertEqual(sum(p["publication_stage"]=="concept" for p in paper),21)
        self.assertTrue(all(p["public_listing"] is False for p in paper))

    def test_modified_local_tex_fails_pinned_blob_validation(self):
        file=self.root/"manuscripts/MSC-AR-P01/main.tex"
        file.write_bytes(file.read_bytes()+b"\n% provenance corruption")
        self.verify_bad("blob SHA")

    def test_canonical_owner_cannot_be_reassigned(self):
        reg=self.papers()
        row=next(p for p in reg["papers"] if p["id"]=="MSC-AR-P01")
        row["owner"]["repository"]="Other/arc-xr"
        self.save("portfolio/papers.json",reg)
        self.verify_bad("local ownership/provenance drift")

    def test_redacted_external_reference_cannot_become_primary(self):
        reg=self.papers()
        row=next(p for p in reg["papers"] if p["id"]=="MSC-ADHD-P04")
        row["relation"]="primary"
        self.save("portfolio/papers.json",reg)
        self.verify_bad("redacted external")

    def test_redacted_external_reference_cannot_approve_public_listing(self):
        reg=self.papers()
        row=next(p for p in reg["papers"] if p["id"]=="MSC-ADHD-P04")
        row["public_listing"]=True
        self.save("portfolio/papers.json",reg)
        self.verify_bad("redacted external")

    def test_status_promotion_without_evidence_rejected(self):
        reg=self.papers()
        row=next(p for p in reg["papers"] if p["id"]=="MSC-AR-P01")
        row["publication_stage"]="published"
        self.save("portfolio/papers.json",reg)
        self.verify_bad("status evidence")

    def test_area_changed_from_pinned_manifest_rejected(self):
        reg=self.papers()
        reg["papers"][0]["area"]="unrelated-area"
        self.save("portfolio/papers.json",reg)
        self.verify_bad("Unknown paper research area")

    def test_duplicate_msc_rejected(self):
        reg=self.papers()
        reg["papers"].append(dict(reg["papers"][0]))
        self.save("portfolio/papers.json",reg)
        self.verify_bad("duplicate MSC")

    def test_historic_six_core_research_state_preserved(self):
        state=self.root/"PROJECT_STATE.yaml"
        body=state.read_text()
        state.write_text(body.replace("planned_core_count: 6","planned_core_count: 5"))
        self.verify_bad("legacy six-paper plan")

    def test_no_duplicate_publication_registry_files(self):
        self.assertFalse((self.root/"portfolio/manuscript_register.md").exists())
        self.assertFalse((self.root/"portfolio/publication_register.md").exists())


if __name__=="__main__":
    unittest.main()
