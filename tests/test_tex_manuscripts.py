"""Kontrola katalogów i indywidualnych źródeł LaTeX ARC-XR."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CORE = {f"MSC-AR-P{i:02d}": f"P{i:02d}" for i in range(1, 7)}
OTHER = (
  "MSC-AAL-P07",
  "MSC-ADHD-P04",
  "MSC-AR-P07",
  "MSC-AR-P08",
  "MSC-AR-P09",
  "MSC-AR-P10",
  "MSC-AR-P11",
  "MSC-AR-P12",
  "MSC-AR-P13",
  "MSC-AR-P14",
  "MSC-AR-P15",
  "MSC-AR-P17",
  "MSC-AR-P18",
  "MSC-AR-P21",
  "MSC-AR-P22",
  "MSC-AR-P23",
  "MSC-AR-P25",
  "MSC-AR-P26",
  "MSC-AR-P27",
  "MSC-AR-P28",
  "MSC-AR-P29"
,)

class TeXManuscriptTests(unittest.TestCase):
    def test_exact_manuscript_coverage(self):
        expected = dict(CORE)
        expected.update({identifier: identifier for identifier in OTHER})
        self.assertEqual(len(expected), 27)
        real = sorted((ROOT / "manuscripts").glob("*/main.tex"))
        self.assertEqual(len(real), 27)
        self.assertEqual({f.parent.name for f in real}, set(expected.values()))
        seen_titles = set()
        for identifier, directory in expected.items():
            tex = ROOT / "manuscripts" / directory / "main.tex"
            with self.subTest(paper=identifier):
                self.assertTrue(tex.is_file())
                self.assertFalse(tex.is_symlink())
                self.assertTrue((tex.parent / "README.md").is_file())
                body = tex.read_text(encoding="utf-8")
                self.assertGreater(len(body), 3500)
                for token in (
                    r"\documentclass", r"\usepackage[T1]{fontenc}",
                    r"\usepackage[polish]{babel}",
                    r"\begin{abstract}", r"\end{abstract}",
                    r"\section{Wprowadzenie}",
                    r"\section{Materiał i metody}",
                    r"\section{Plan analizy}",
                    r"\section{Wyniki}",
                    r"\section{Ograniczenia badania}",
                    r"\end{document}",
                ):
                    self.assertIn(token, body)
                self.assertIn("% Portfolio: " + identifier + ";", body)
                match = re.search(r"\\title\{(.+)\}", body)
                self.assertIsNotNone(match)
                self.assertNotIn(match.group(1), seen_titles)
                seen_titles.add(match.group(1))
                self.assertEqual(body.count(r"\begin{document}"), 1)
                self.assertEqual(body.count(r"\end{document}"), 1)

    def test_core_protocols_and_public_pages_remain_separate(self):
        for directory in CORE.values():
            self.assertTrue((ROOT / "manuscripts" / directory / "protocol/README.md").is_file())
        from json import loads
        policy = loads((ROOT / "config/pages-policy.json").read_text(encoding="utf-8"))
        self.assertEqual(policy["source_dir"], "pages")
        self.assertNotIn("manuscripts", policy["public_files"])

if __name__ == "__main__":
    unittest.main()
