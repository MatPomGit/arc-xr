"""Offline ARC-XR GitHub Issue form and autonomy contract validator."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"01-task.yml": None, "02-bug.yml": "[fix]",
            "03-experiment.yml": "[experiment]", "04-manuscript.yml": "[paper]"}
MANDATORY = {"acceptance", "verification", "gates", "next_step"}


def check_issues(root: Path = ROOT) -> list[str]:
    root = Path(root).resolve()
    findings = []
    try:
        data = json.loads((root / "config/issues-policy.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError):
        return ["ISSUES POLICY: missing or malformed JSON"]
    if not isinstance(data, dict) or type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        return ["ISSUES POLICY: unsupported schema_version"]
    if data.get("enable_agent_dispatch") is not False or data.get("create_labels_automatically") is not False:
        findings.append("ISSUES POLICY: labels and dispatch must stay disabled")
    if data.get("classification_marker") != "agent-work-classification:v1":
        findings.append("ISSUES POLICY: classification marker mismatch")
    templates = data.get("templates")
    if (not isinstance(templates, list) or len(templates) != len(EXPECTED)
            or not all(isinstance(item, dict) for item in templates)
            or [item.get("file") for item in templates] != list(EXPECTED)):
        return sorted(set(findings + ["ISSUES POLICY: unsupported template list"]))
    folder = root / ".github/ISSUE_TEMPLATE"
    if not folder.is_dir() or folder.is_symlink():
        return sorted(set(findings + ["ISSUES SOURCE: missing or unsafe directory"]))
    for path in folder.rglob("*"):
        rel = path.relative_to(folder).as_posix()
        if path.is_symlink():
            findings.append("ISSUES SYMLINK: " + rel)
        elif path.is_file() and rel not in set(EXPECTED) | {"config.yml"}:
            findings.append("ISSUES UNREVIEWED FORM: " + rel)
    config = folder / "config.yml"
    if not config.is_file() or config.is_symlink():
        findings.append("ISSUES CONFIG: missing config.yml")
    else:
        try:
            cfg = config.read_text(encoding="utf-8")
            if not re.search(r"(?m)^blank_issues_enabled:\s*false\s*$", cfg):
                findings.append("ISSUES CONFIG: blank issues must remain disabled")
            if "https://github.com/MatPomGit/arc-xr/blob/main/SECURITY.md" not in cfg:
                findings.append("ISSUES CONFIG: security contact link missing")
        except (OSError, UnicodeError):
            findings.append("ISSUES CONFIG: unreadable")
    for item in templates:
        name = item["file"]
        path = folder / name
        if name not in EXPECTED or not path.is_file() or path.is_symlink():
            findings.append("ISSUES FORM: missing or unsafe " + str(name))
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            findings.append("ISSUES FORM: unreadable " + name)
            continue
        if not all(re.search(r"(?m)^" + key + r":\s*.+$", content)
                   for key in ("name", "description")) or not re.search(r"(?m)^body:\s*$", content):
            findings.append("ISSUES FORM: missing GitHub form fields " + name)
        if re.search(r"(?m)^(labels|assignees):\s*", content):
            findings.append("ISSUES FORM: automatic metadata is not authorized " + name)
        match = re.search(r'(?m)^title:\s*["' + "'" + r']?(\[[a-z0-9]+\])', content)
        tag = match.group(1) if match else None
        if item.get("intent_tag") != EXPECTED[name] or tag != EXPECTED[name]:
            findings.append("ISSUES FORM: invalid task intent " + name)
        fields = {}
        for block in re.split(r"(?m)^  - type: ", content)[1:]:
            if not block.startswith("textarea"):
                continue
            found = re.search(r"(?m)^    id:\s*([a-z][a-z0-9_]*)\s*$", block)
            if not found:
                findings.append("ISSUES FORM: textarea without id " + name)
                continue
            identifier = found.group(1)
            if identifier in fields:
                findings.append("ISSUES FORM: duplicate field id " + name)
            fields[identifier] = block
        required = item.get("required_fields")
        if (not isinstance(required, list) or not all(isinstance(x, str) for x in required)
                or not MANDATORY.issubset(required)):
            findings.append("ISSUES POLICY: required fields invalid " + name)
            continue
        if "classification" not in fields or "relations" not in fields:
            findings.append("ISSUES FORM: classification or relations missing " + name)
        for identifier in required:
            if identifier not in fields or not re.search(r"(?m)^      required:\s*true\s*$", fields[identifier]):
                findings.append("ISSUES FORM: required field absent or optional " + name + "/" + identifier)
    try:
        docs = (root / "docs/issues.md").read_text(encoding="utf-8")
        if not all(x in docs for x in ("agent-work-classification:v1", "NATIVE_RELATIONS_NOT_APPLIED",
                                      "TASK_TYPES.md", "LABEL_TAXONOMY.md", "GITHUB_WORK_MANAGEMENT.md")):
            findings.append("ISSUES DOCS: central standards or native-relations warning missing")
    except (OSError, UnicodeError):
        findings.append("ISSUES DOCS: missing or unreadable")
    for name in ("AGENTS.md", ".github/AGENT_WORKFLOW.md"):
        try:
            if "docs/issues.md" not in (root / name).read_text(encoding="utf-8"):
                findings.append("ISSUES DOCS: missing workflow link in " + name)
        except (OSError, UnicodeError):
            findings.append("ISSUES DOCS: missing " + name)
    return sorted(set(findings))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    problems = check_issues(parser.parse_args().root)
    for issue in problems:
        print("FAIL:", issue)
    print("arc-xr-issues:", "FAIL" if problems else "PASS")
    return int(bool(problems))


if __name__ == "__main__":
    raise SystemExit(main())
