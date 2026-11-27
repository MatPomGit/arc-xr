"""Validate active v3 metadata and preserve historical v2 scientific evidence."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

def main():
    Draft202012Validator(load("schemas/program.v3.schema.json")).validate(load("program.json"))
    validator = Draft202012Validator(load("schemas/paper.v3.schema.json"))
    old = {r["id"]: r for r in load("migration/provenance/papers-v2.json")["papers"]}
    paths = sorted(ROOT.glob("manuscripts/MSC-*/paper.json"))
    assert {p.parent.name for p in paths} == set(old)
    for path in paths:
        record = load(path.relative_to(ROOT))
        validator.validate(record)
        assert record["id"] == path.parent.name
        for key in ("owner", "relation", "publication_stage", "research_state", "public_listing", "manuscript"):
            assert record[key] == old[record["id"]][key], (record["id"], key)
        if record["study_plan"]:
            assert (ROOT / record["study_plan"]).is_file()
    print(f"PASS: {len(paths)} v3 records")
if __name__ == "__main__":
    main()
