"""Walidacja wygenerowanej zawartości statycznej ARC-XR."""
from pathlib import Path
import re
import sys

PAGES = ("index", "articles", "adaptation", "affect",
         "perception", "procedures", "collaboration")

def validate(site: Path) -> list[str]:
    if not site.is_dir() or site.is_symlink():
        return ["Brak bezpiecznego katalogu witryny"]
    errors = []
    for page in PAGES:
        html = site / ("index.html" if page == "index" else page + "/index.html")
        if not html.is_file() or html.is_symlink():
            errors.append("Brak wygenerowanej strony: " + page)
    forbidden = re.compile(
        r"AGENT_WORKFLOW|CONTRIBUTING[.]md|research-autopilot|"
        r"MatPomGit/devices|neuro_paper_slots|"
        r"/docs/(?:security|adr)/|/manuscripts/P[0-9]+/",
        flags=re.IGNORECASE,
    )
    for html in site.rglob("*.html"):
        if html.is_symlink() or forbidden.search(html.read_text(encoding="utf-8")):
            errors.append("Niedozwolona treść wynikowa: " + str(html.relative_to(site)))
    return errors

if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "site")
    problems = validate(root)
    for issue in problems:
        print("FAIL:", issue)
    print("arc-xr-site:", "FAIL" if problems else "PASS")
    raise SystemExit(bool(problems))
