"""Validate ARC-XR v2 registries, pinned TeX and retained legacy research state."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from jsonschema import Draft202012Validator
from validate_registry_v2 import validate_registry_v2
from validate_repository import state_ids
from audit_arc_v2_pilot import audit as audit_sources

ROOT=Path(__file__).resolve().parents[1]
MAP={"program.json":"schemas/program.v2.schema.json",
     "portfolio/projects.json":"schemas/projects.v2.schema.json",
     "portfolio/papers.json":"schemas/papers.v2.schema.json",
     "portfolio/dependencies.json":"schemas/dependencies.v2.schema.json"}

def read(root,rel):
    path=root/rel
    if path.is_symlink() or not path.is_file() or path.stat().st_size>2000000:
        raise ValueError("unsafe or missing file: "+rel)
    return json.loads(path.read_text(encoding="utf-8"))

def no_unreviewed_url(_):
    return False  # All imported source records must initially contain no public URL.

def audit(root:Path=ROOT)->list[str]:
    root=Path(root).absolute()
    errors=[]
    try:
        values={name:read(root,name) for name in
                ("program.json","portfolio/projects.json","portfolio/papers.json",
                 "portfolio/dependencies.json","areas/index.json",
                 "migration/arc-v2-pilot-map.json","migration/provenance/source-manifest-v1.json")}
        for rel,schema_rel in MAP.items():
            schema=read(root,schema_rel)
            Draft202012Validator.check_schema(schema)
            for issue in Draft202012Validator(schema).iter_errors(values[rel]):
                errors.append("ARC_V2_SCHEMA "+rel+": "+issue.message)
    except (OSError,ValueError,KeyError,TypeError) as exc:
        return ["ARC_V2_METADATA "+type(exc).__name__+": "+str(exc)]
    meta=values["program.json"]
    registry=values["portfolio/papers.json"]
    projects=values["portfolio/projects.json"]
    deps=values["portfolio/dependencies.json"]
    areas=values["areas/index.json"]
    if not all(isinstance(obj,dict) for obj in (meta,registry,projects,deps,areas)):
        return ["ARC_V2_METADATA: required JSON objects"]
    if meta.get("repository_full_name")!="MatPomGit/arc-xr" or meta.get("programme")!="arc-xr":
        errors.append("ARC_V2_IDENTITY: owner must equal canonical ARC-XR")
    if meta.get("repository_visibility")!="public" or meta.get("manuscript_root")!="manuscripts":
        errors.append("ARC_V2_CONFIG: unexpected repository visibility/root")
    records=registry.get("papers")
    project_rows=projects.get("projects")
    if not isinstance(records,list) or not isinstance(project_rows,list):
        return errors+["ARC_V2_METADATA: missing paper/project arrays"]
    project_repos={x.get("id"):x.get("repository") for x in project_rows if isinstance(x,dict)}
    lines={a.get("id") for a in areas.get("lines",[]) if isinstance(a,dict)}
    if len(lines)!=5:
        errors.append("ARC_V2_AREAS: expected five scientific areas")
    errors.extend(validate_registry_v2(root,meta,records,deps,project_repos,
                                       lines,no_unreviewed_url))
    mapping=values["migration/arc-v2-pilot-map.json"].get("records")
    prior=values["migration/provenance/source-manifest-v1.json"].get("papers")
    if not isinstance(mapping,list) or not isinstance(prior,list):
        return errors+["ARC_V2_MAPPING: missing historical source manifest"]
    byid={p.get("id"):p for p in records if isinstance(p,dict)}
    old={p.get("id"):p for p in prior if isinstance(p,dict)}
    pinned={p.get("id"):p for p in mapping if isinstance(p,dict)}
    if any(len(x)!=27 for x in (byid,old,pinned)) or not (set(byid)==set(old)==set(pinned)):
        errors.append("ARC_V2_COVERAGE: exactly 27 unique entries required")
    local=related=0
    for ident,p in byid.items():
        source=old.get(ident)
        pin=pinned.get(ident)
        if not isinstance(source,dict) or not isinstance(pin,dict):
            continue
        if p.get("title")!=source.get("title") or p.get("area")!=pin.get("area"):
            errors.append("ARC_V2_SOURCE: title/area drift "+str(ident))
        owner=p.get("owner")
        if not isinstance(owner,dict):
            continue
        if pin.get("ownership")=="local":
            local+=1
            tex=p.get("manuscript")
            if (owner!={"mode":"local","repository":"MatPomGit/arc-xr","project_id":None}
                    or p.get("relation")!="primary" or not isinstance(tex,dict)
                    or tex.get("path")!=pin.get("to")
                    or tex.get("blob_sha")!=pin.get("blob_sha")):
                errors.append("ARC_V2_SOURCE: local ownership/provenance drift "+str(ident))
        elif pin.get("ownership")=="external_companion":
            related+=1
            if (owner!={"mode":"external","repository":None,"project_id":None,"redacted":True}
                    or p.get("relation")!="related" or p.get("manuscript") is not None):
                errors.append("ARC_V2_SOURCE: invalid redacted external relation "+str(ident))
        if p.get("public_listing") is not False:
            errors.append("ARC_V2_DISCLOSURE: migration cannot approve listings")
        if p.get("publication_stage")!=("draft" if source.get("category")=="MANUSCRIPT" else "concept"):
            errors.append("ARC_V2_STAGE: unverified publication promotion "+str(ident))
    if local!=26 or related!=1:
        errors.append("ARC_V2_OWNERSHIP: expected 26 local and one related")
    try:
        core=state_ids((root/"PROJECT_STATE.yaml").read_text(encoding="utf-8"))
    except (OSError,UnicodeError):
        core=None
    if core!=([f"P{i:02d}" for i in range(1,7)],6):
        errors.append("ARC_V2_LEGACY_STATE: legacy six-paper plan changed")
    errors.extend(audit_sources(root))
    return sorted(set(errors))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=ROOT)
    args=parser.parse_args()
    errors=audit(args.root)
    for error in errors:
        print("FAIL:",error)
    print("arc-xr-v2:", "FAIL" if errors else "PASS")
    return 1 if errors else 0

if __name__=="__main__":
    raise SystemExit(main())
