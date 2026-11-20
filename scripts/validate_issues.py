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



# Contract source: research-autopilot/docs/autonomy/agent-work-classification.md.
# This checker guards shape and authorization invariants only. The central
# catalogue, not this source, remains authoritative for labels and task intents.
META_KEYS = (
    "work_types", "execution_mode", "human_approval_required",
    "human_approval_reasons", "resource_requirements",
    "autonomous_scope", "human_required_scope",
)
MODES = {"autonomous", "autonomous_with_runtime", "mixed", "human_required"}
START_MARKER = "<!-- agent-work-classification:v1 -->"
END_MARKER = "<!-- /agent-work-classification -->"


def check_classification(text: str) -> list[str]:
    """Validate one bounded v1 block from an Issue body, without execution."""
    problems: list[str] = []
    if text.count(START_MARKER) != 1 or text.count(END_MARKER) != 1:
        return ["CLASSIFICATION: requires exactly one complete v1 block"]
    start = text.find(START_MARKER) + len(START_MARKER)
    end = text.find(END_MARKER)
    if end <= start:
        return ["CLASSIFICATION: invalid marker order"]
    body = text[start:end].strip()
    values: dict[str, str] = {}
    for line in body.splitlines():
        matched = re.fullmatch(r"([a-z][a-z_]*):[ \t]+(.+)", line)
        if not matched:
            problems.append("CLASSIFICATION: malformed field")
            continue
        key, value = matched.groups()
        if key not in META_KEYS or key in values:
            problems.append("CLASSIFICATION: unknown or duplicate field " + key)
        values[key] = value.strip()
    if set(values) != set(META_KEYS):
        problems.append("CLASSIFICATION: missing or extra fields")
        return sorted(set(problems))
    mode = values["execution_mode"]
    if mode not in MODES:
        problems.append("CLASSIFICATION: unknown execution_mode")
    approval = values["human_approval_required"]
    if approval not in ("true", "false"):
        problems.append("CLASSIFICATION: approval must be boolean")
    def parse_array(key: str) -> list[str] | None:
        value = values[key]
        if not (value.startswith("[") and value.endswith("]")):
            problems.append("CLASSIFICATION: invalid array " + key)
            return None
        tokens = [z.strip() for z in value[1:-1].split(",")]
        if len(tokens) == 1 and tokens[0] == "":
            return []
        if any(not re.fullmatch(r"[a-z][a-z_]*", z) for z in tokens) or len(set(tokens)) != len(tokens):
            problems.append("CLASSIFICATION: invalid tokens " + key)
            return None
        return tokens
    types = parse_array("work_types")
    reasons = parse_array("human_approval_reasons")
    resources = parse_array("resource_requirements")
    if types is not None and not types:
        problems.append("CLASSIFICATION: work_types must not be empty")
    if resources is not None and not resources:
        problems.append("CLASSIFICATION: resource_requirements must not be empty")
    if reasons is not None:
        if approval == "true" and not reasons:
            problems.append("CLASSIFICATION: human approval needs a reason")
        if approval == "false" and reasons:
            problems.append("CLASSIFICATION: approval reason contradicts false")
    if mode in {"mixed", "human_required"} and approval != "true":
        problems.append("CLASSIFICATION: human gate required by execution_mode")
    if any(not (values[key].startswith('"') and values[key].endswith('"')) for key in ("autonomous_scope", "human_required_scope")):
        problems.append("CLASSIFICATION: scopes must be quoted strings")
    human_scope = values["human_required_scope"]
    if approval == "true" and human_scope in ('"none"', '""'):
        problems.append("CLASSIFICATION: human scope missing")
    if approval == "false" and human_scope != '"none"':
        problems.append("CLASSIFICATION: unsupported human scope without approval")
    return sorted(set(problems))


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
    if data.get("require_verified_native_relationships") is not False:
        findings.append("ISSUES POLICY: cannot claim unverified native relations")
    if data.get("security_policy") != "SECURITY.md":
        findings.append("ISSUES POLICY: incorrect security contract")
    source = "MatPomGit/research-autopilot/"
    for key, target in (
        ("source_of_truth", "docs/architecture/GITHUB_WORK_MANAGEMENT.md"),
        ("classification_contract", "docs/autonomy/agent-work-classification.md"),
        ("task_intents", "docs/autonomy/TASK_TYPES.md"),
        ("labels_taxonomy", "docs/LABEL_TAXONOMY.md"),
    ):
        if data.get(key) != source + target:
            findings.append("ISSUES POLICY: central contract drift " + key)
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
