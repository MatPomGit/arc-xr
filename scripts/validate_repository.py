"""Offline structural validation of the actual ARC-XR research programme.

No network requests, scientific status promotion, participant data, or write operations.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_documentation import check_documentation
from validate_pages import check_pages
from validate_issues import check_issues
from audit_arc_v2_pilot import audit as audit_arc_v2_pilot

REQUIRED = (
    "AGENTS.md", ".github/AGENT_WORKFLOW.md",
    "ARCHITECTURE.md", "SECURITY.md", "CODE_OF_CONDUCT.md",
    "GOVERNANCE.md", "SUPPORT.md",
    "README.md", "RESEARCH.md", "REPRODUCIBILITY.md",
    "AUTOPILOT_PLAN.md", "PROJECT_STATE.yaml",
    "manuscripts/README.md", "manuscripts/mvp_plan.md",
    "config/documentation-policy.json", "config/pages-policy.json",
    "scripts/validate_repository.py", "scripts/validate_documentation.py",
    "scripts/validate_pages.py", "scripts/validate_issues.py",
    "config/issues-policy.json", "docs/issues.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/01-task.yml", ".github/ISSUE_TEMPLATE/02-bug.yml",
    ".github/ISSUE_TEMPLATE/03-experiment.yml", ".github/ISSUE_TEMPLATE/04-manuscript.yml",
    "tests/test_issues_policy.py",
    "scripts/audit_arc_v2_pilot.py",
    "migration/arc-v2-pilot-map.json",
    "tests/test_arc_v2_pilot.py",
    "docs/migrations/arc-v2-pilot.md",
    "docs/index.md", "docs/documentation.md", "docs/pages.md",
    "docs/architecture/README.md", "docs/architecture/components.md",
    "docs/architecture/data-flow.md",
    "docs/architecture/measurement-boundaries.md",
    "docs/security/threat-model.md", "docs/security/incident-response.md",
    "docs/operations/runbook.md", "docs/adr/README.md",
    "docs/adr/0001-programme-boundaries.md",
    "docs/adr/0002-research-and-device-safety.md",
    "docs/adr/0003-public-pages-boundary.md",
    "site/index.md", "mkdocs.yml",
    ".github/workflows/quality.yml",
    "tests/test_repository_contract.py", "tests/test_documentation_policy.py",
    "tests/test_pages_policy.py",
)

MANUSCRIPT_FILES = (
    "README.md", "manuscript.md", "references.bib",
    "hypotheses/README.md", "protocol/README.md",
    "experiments/README.md", "analyses/README.md",
    "results/README.md", "figures/README.md",
)


def state_ids(text: str) -> tuple[list[str], int] | None:
    """Read only the canonical scalar and inline-list fields; no YAML dependency."""
    matched_ids = re.search(r"(?m)^\s*planned_ids:\s*\[([^\]]+)\]\s*$", text)
    matched_count = re.search(r"(?m)^\s*planned_core_count:\s*(\d+)\s*$", text)
    if not matched_ids or not matched_count:
        return None
    raw = matched_ids.group(1).split(",")
    ids = [item.strip().strip("\"'") for item in raw]
    if not ids or any(not re.fullmatch(r"P\d{2}", item) for item in ids):
        return None
    return ids, int(matched_count.group(1))


def check_repository(root: Path = ROOT) -> list[str]:
    root = Path(root).resolve()
    problems: list[str] = []
    for rel in REQUIRED:
        path = root / rel
        if path.is_symlink() or not path.is_file():
            problems.append("ARC REQUIRED: missing or symlink " + rel)
    if (root / "CONTRIBUTING.md").exists():
        problems.append("ARC POLICY: no CONTRIBUTING.md")
    try:
        state = (root / "PROJECT_STATE.yaml").read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        problems.append("ARC STATE: missing or unreadable PROJECT_STATE.yaml")
        state = ""
    values = state_ids(state)
    if values is None:
        problems.append("ARC STATE: missing or invalid planned publication IDs/count")
    else:
        identifiers, count = values
        if len(identifiers) != count or len(set(identifiers)) != len(identifiers):
            problems.append("ARC STATE: planned publication count or IDs inconsistent")
        for identifier in identifiers:
            for name in MANUSCRIPT_FILES:
                file = root / "manuscripts" / ("MSC-AR-" + identifier) / name
                if not file.is_file() or file.is_symlink():
                    problems.append(f"ARC MANUSCRIPT: missing {identifier}/{name}")
    problems.extend(check_documentation(root))
    problems.extend(check_pages(root))
    problems.extend(check_issues(root))
    problems.extend(audit_arc_v2_pilot(root))
    return sorted(set(problems))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    problems = check_repository(args.root)
    for problem in problems:
        print("FAIL:", problem)
    print("arc-xr-contract:", "FAIL" if problems else "PASS")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
