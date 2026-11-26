"""ARC-XR E4.0 regression tests: 27 prospective papers and provenance.

These are structural checks. They do not certify a clinical protocol or evidence.
"""
from __future__ import annotations
import json
from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]
MANUSCRIPTS=ROOT/"manuscripts"
MANIFEST=json.loads((ROOT/"migration/provenance/source-manifest-v1.json").read_text(encoding="utf-8"))
PAPERS=MANIFEST["papers"]
LITERATURE=json.loads((MANUSCRIPTS/"literature"/"prior_art_sources.json").read_text(encoding="utf-8"))["references"]

class XRResearchProtocolTest(unittest.TestCase):
    def test_registry_and_structure(self):
        self.assertEqual(len(PAPERS),27)
        self.assertEqual(len({p["id"] for p in PAPERS}),27)
        self.assertEqual(len({p["folder"] for p in PAPERS}),27)
        self.assertEqual(sum(p["id"] in {f"MSC-AR-P{i:02d}" for i in range(1,7)} for p in PAPERS),6)
        self.assertEqual(sum(p["category"]=="MANUSCRIPT" for p in PAPERS),7)
        self.assertEqual(sum(p["category"]=="CANDIDATE" for p in PAPERS),20)

    def test_hypotheses_four_stages_and_bibliography(self):
        for p in PAPERS:
            with self.subTest(id=p["id"]):
                source=(ROOT/p["local_draft"]).read_text(encoding="utf-8")
                if p["id"] == "MSC-ADHD-P04":
                    folder = ROOT / p["local_draft"]
                    self.assertIn(r"\documentclass[man]{apa7}", source)
                    self.assertIn(r"\authorsnames{Mateusz Pomianek}", source)
                    self.assertIn(r"\addbibresource{references.bib}", source)
                    self.assertTrue((folder.parent / "references.bib").is_file())
                    sections = re.findall(r"\\input\{(sections/[^}]+)\}", source)
                    self.assertEqual(len(sections), 15)
                    self.assertEqual(len(set(sections)), 15)
                    for section in sections:
                        self.assertTrue((folder.parent / (section + ".tex")).is_file())
                    self.assertEqual(source.count(r"\begin{document}"), 1)
                    self.assertEqual(source.count(r"\end{document}"), 1)
                    continue
                expected_version = {"MSC-AR-P04": "0.4.0"}.get(p["id"], "0.3.0")
                self.assertRegex(source, r"\\date\{Wersja " + re.escape(expected_version) + r",")
                self.assertEqual(re.findall(r"\\paragraph\{H([1-3])\.\}",source),["1","2","3"])
                self.assertEqual(re.findall(r"\\subsection\{([A-D])\. ",source),["A","B","C","D"])
                for section in ("Zakres i odrębny wkład naukowy",
                                "Hipotezy badawcze",
                                "Projekt badania i plan eksperymentów",
                                "Estymand, analiza statystyczna i decyzje",
                                "Stan badań i granica nowości",
                                "Warunki bezpieczeństwa, sprzętu i zgodności"):
                    self.assertIn(r"\section{"+section+"}",source)
                self.assertEqual(len(re.findall(r"\\bibitem\{xrprior[12]\}",source)),2)
                self.assertEqual(len(re.findall(r"\\cite\{xrprior[12]\}",source)),2)
                self.assertEqual(source.count(r"\begin{document}"),1)
                self.assertEqual(source.count(r"\end{document}"),1)

    def test_pinned_scientific_source_and_nonpromotion(self):
        for p in PAPERS:
            with self.subTest(id=p["id"]):
                if p["local_draft_role"]=="cross_program_companion_plan":
                    self.assertEqual(p["owner_programme"],"external")
                    for key in ("source_repository","source_path","source_sha","source_url"):
                        self.assertIsNone(p[key])
                else:
                    self.assertEqual(p["owner_programme"],"arc-xr")
                    self.assertRegex(p["source_sha"],r"^[0-9a-f]{40}$")
                    url=f"https://github.com/{p['source_repository']}/blob/{p['source_sha']}/{p['source_path']}"
                    self.assertEqual(p["source_url"],url)
                self.assertEqual(p["local_draft"],f"manuscripts/{p['folder']}/main.tex")
                self.assertTrue((ROOT/p["local_draft"]).is_file())
                self.assertIn(p["local_draft_role"],("core_research_plan","unapproved_concept_plan","cross_program_companion_plan"))
                self.assertNotEqual(p["scientific_status"],"PUBLISHED")
        cross=next(p for p in PAPERS if p["id"]=="MSC-ADHD-P04")
        self.assertEqual(cross["owner_programme"],"external")
        self.assertIsNone(cross["source_repository"])
        self.assertEqual(cross["local_draft_role"],"cross_program_companion_plan")

    def test_prior_art_matrix_complete(self):
        self.assertGreaterEqual(len(LITERATURE),18)
        for ref in LITERATURE.values():
            self.assertTrue(ref["title"] and ref["scope"])
            self.assertTrue(ref["url"].startswith("https://"))
        matrix=(MANUSCRIPTS/"literature"/"novelty_matrix.md").read_text(encoding="utf-8")
        rows=re.findall(r"^\| \[(MSC-[A-Z0-9]+-P\d+)\]",matrix,flags=re.MULTILINE)
        self.assertEqual(len(rows),27)
        self.assertEqual(set(rows),{p["id"] for p in PAPERS})

    def test_public_pages_not_contaminated(self):
        self.assertTrue((ROOT/"pages"/"index.md").exists())
        self.assertFalse((ROOT/".github"/"workflows"/"publish-pages.yml").exists())
        self.assertFalse((ROOT/".github"/"workflows"/"deploy-pages.yml").exists())

if __name__=="__main__":
    unittest.main()
