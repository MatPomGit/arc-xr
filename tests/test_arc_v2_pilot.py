"""Regression tests for read-only ARC XR v2 preflight."""
from __future__ import annotations
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from audit_arc_v2_pilot import audit


class PilotTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)/"arc"
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns(".git","site","__pycache__"))
    def tearDown(self):
        self.temp.cleanup()
    def load(self,name):
        return json.loads((self.root/name).read_text())
    def save(self,name,obj):
        (self.root/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n")

    def test_baseline(self):
        self.assertEqual([],audit(ROOT))
        self.assertEqual([],audit(self.root))

    def test_26_local_1_external_6_renames(self):
        rows=self.load("migration/arc-v2-pilot-map.json")["records"]
        self.assertEqual(len(rows),27)
        self.assertEqual(len(set(x["id"] for x in rows)),27)
        self.assertEqual(sum(x["ownership"]=="local" for x in rows),26)
        self.assertEqual(sum(x["ownership"]=="external_companion" for x in rows),1)
        self.assertEqual(sum(x["from"]!=x["to"] for x in rows),6)

    def test_external_metadata_is_redacted(self):
        papers=self.load("migration/provenance/source-manifest-v1.json")["papers"]
        cross=[x for x in papers if x["local_draft_role"]=="cross_program_companion_plan"]
        self.assertEqual(len(cross),1)
        self.assertEqual(cross[0]["owner_programme"],"external")
        self.assertTrue(all(cross[0][key] is None
                            for key in ("source_repository","source_path","source_sha","source_url")))

    def test_tampered_tex_sha_rejected(self):
        file=self.root/"manuscripts/MSC-AR-P01/main.tex"
        file.write_bytes(file.read_bytes()+b"\n% tamper")
        self.assertTrue(any("source SHA mismatch" in x for x in audit(self.root)))

    def test_missing_manuscript_rejected(self):
        (self.root/"manuscripts/MSC-AR-P02/main.tex").unlink()
        self.assertTrue(any("missing/symlink manuscript" in x for x in audit(self.root)))

    def test_destination_collision_rejected(self):
        path=self.root/"manuscripts/P01"
        path.mkdir()
        (path/"main.tex").write_text("legacy document")
        self.assertTrue(any("legacy source not removed" in x for x in audit(self.root)))

    def test_duplicate_id_rejected(self):
        path="migration/arc-v2-pilot-map.json"
        mapping=self.load(path)
        mapping["records"][1]["id"]=mapping["records"][0]["id"]
        self.save(path,mapping)
        self.assertTrue(any("duplicate" in x for x in audit(self.root)))

    def test_area_mismatch_rejected(self):
        path="migration/arc-v2-pilot-map.json"
        mapping=self.load(path)
        mapping["records"][0]["area"]="affect"
        self.save(path,mapping)
        self.assertTrue(any("wrong scientific area" in x for x in audit(self.root)))

    def test_private_owner_leak_rejected(self):
        path="migration/provenance/source-manifest-v1.json"
        manifest=self.load(path)
        cross=next(x for x in manifest["papers"]
                   if x["local_draft_role"]=="cross_program_companion_plan")
        cross["source_repository"]="private/undisclosed"
        self.save(path,manifest)
        self.assertTrue(any("private source metadata not redacted" in x
                            for x in audit(self.root)))

    def test_extra_source_rejected(self):
        path=self.root/"manuscripts/MSC-TEST-P99"
        path.mkdir()
        (path/"main.tex").write_text("unexpected")
        self.assertTrue(any("incomplete local sources" in x for x in audit(self.root)))

    def test_does_not_write_files(self):
        names=["migration/arc-v2-pilot-map.json","migration/provenance/source-manifest-v1.json",
               "manuscripts/MSC-AR-P01/main.tex"]
        before={name:(self.root/name).read_bytes() for name in names}
        self.assertEqual([],audit(self.root))
        self.assertEqual(before,{name:(self.root/name).read_bytes() for name in names})


if __name__=="__main__":
    unittest.main()
