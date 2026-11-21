"""Kontrola kompletności opisów publikacji na publicznej stronie ARC-XR."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "adaptation": (11, 1),
    "affect": (6, 2),
    "perception": (4, 2),
    "procedures": (3, 1),
    "collaboration": (3, 1),
}

class ArticlesCatalogTests(unittest.TestCase):
    def test_articles_and_stages(self):
        seen = set()
        manuscript_total = 0
        concept_total = 0
        for category, (count, manuscript_count) in CATEGORIES.items():
            page = (ROOT / "pages" / (category + ".md")).read_text(encoding="utf-8")
            self.assertIn("## Planowane manuskrypty", page)
            self.assertIn("## Koncepcje badawcze", page)
            items = re.findall(
                r"^### ([^\n]+)\n\n(.+?)(?=\n\n(?:### |## |\[Wszystkie)|\Z)",
                page, flags=re.MULTILINE | re.DOTALL
            )
            self.assertEqual(len(items), count, category)
            for title, summary in items:
                self.assertNotIn(title, seen)
                seen.add(title)
                self.assertGreaterEqual(len(summary.strip()), 90)
                self.assertNotRegex(summary, r"MSC-[A-Z0-9]+-[PRS]\d+|slot-\d+")
            core = page.split("## Koncepcje badawcze", 1)[0]
            actual_core = len(re.findall(r"^### ", core, flags=re.MULTILINE))
            self.assertEqual(actual_core, manuscript_count, category)
            manuscript_total += actual_core
            concept_total += count - actual_core
        self.assertEqual(len(seen), 27)
        self.assertEqual((manuscript_total, concept_total), (7, 20))

    def test_catalog_navigation(self):
        index = (ROOT / "pages/articles.md").read_text(encoding="utf-8")
        home = (ROOT / "pages/index.md").read_text(encoding="utf-8")
        self.assertIn("27 tematów", index)
        self.assertIn("articles.md", home)
        for category in CATEGORIES:
            self.assertIn("](" + category + ".md)", index)

if __name__ == "__main__":
    unittest.main()
