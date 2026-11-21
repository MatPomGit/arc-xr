"""Read-only ARC v2 migration preflight; verify SHA and ownership without writes."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ID=re.compile(r"^MSC-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
SHA=re.compile(r"^[0-9a-f]{40}$")
AREAS=("adaptation","affect","perception","procedures","collaboration")


def git_blob_sha(path: Path) -> str:
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\x00"+data).hexdigest()


def audit(root: Path = ROOT) -> list[str]:
    root=Path(root).absolute()
    issues=[]
    try:
        plan=json.loads((root/"migration/arc-v2-pilot-map.json").read_text())
        manifest=json.loads((root/"manuscripts/source_manifest.json").read_text())
    except (OSError,ValueError):
        return ["PILOT: unreadable mapping or manifest"]
    if (plan.get("schema_version")!=1 or plan.get("programme")!="arc-xr"
        or plan.get("intent")!="SOURCE_PATHS_MIGRATED"
        or not isinstance(plan.get("source_main_sha"),str)
        or not SHA.fullmatch(plan["source_main_sha"])):
        return ["PILOT: invalid plan header"]
    records=plan.get("records")
    papers=manifest.get("papers")
    if not isinstance(records,list) or not isinstance(papers,list):
        return ["PILOT: expected article lists"]
    byid={p.get("id"):p for p in papers if isinstance(p,dict)}
    if len(records)!=27 or len(papers)!=27 or len(byid)!=27:
        issues.append("PILOT: 27 unique sources expected")
    public={}
    for area in AREAS:
        page=root/"pages"/(area+".md")
        if not page.is_file() or page.is_symlink():
            issues.append("PILOT: missing category: "+area)
            continue
        for title in re.findall(r"^### (.+)$",page.read_text(),re.M):
            if title in public:
                issues.append("PILOT: duplicate public scientific title")
            public[title]=area
    seen=set()
    source_paths=set()
    target_paths=set()
    rename=companion=0
    for item in records:
        if not isinstance(item,dict):
            issues.append("PILOT: malformed record")
            continue
        ident=item.get("id")
        if not isinstance(ident,str) or not ID.fullmatch(ident) or ident in seen:
            issues.append("PILOT: duplicate or malformed MSC identifier")
            continue
        seen.add(ident)
        source=byid.get(ident)
        if source is None:
            issues.append("PILOT: missing source record "+ident)
            continue
        frm=item.get("from")
        to=item.get("to")
        if not all(isinstance(x,str) and x.startswith("manuscripts/")
                   and x.endswith("/main.tex") and "\\" not in x
                   and all(part not in ("","..",".") for part in x.split("/"))
                   for x in (frm,to)):
            issues.append("PILOT: unsafe path "+ident)
            continue
        if frm in source_paths or to in target_paths:
            issues.append("PILOT: duplicate source or destination")
        source_paths.add(frm)
        target_paths.add(to)
        f=root/to
        if f.is_symlink() or not f.is_file() or not f.resolve().is_relative_to(root):
            issues.append("PILOT: missing/symlink manuscript "+ident)
            continue
        blob=item.get("blob_sha")
        if not isinstance(blob,str) or not SHA.fullmatch(blob) or git_blob_sha(f)!=blob:
            issues.append("PILOT: source SHA mismatch "+ident)
        if source.get("local_draft")!=to or source.get("local_draft_role")!=item.get("source_role"):
            issues.append("PILOT: changed source mapping "+ident)
        if public.get(source.get("title"))!=item.get("area"):
            issues.append("PILOT: wrong scientific area "+ident)
        if item.get("ownership")=="local":
            if to!="manuscripts/"+ident+"/main.tex":
                issues.append("PILOT: invalid canonical target "+ident)
            if source.get("source_repository")!="MatPomGit/arc-xr":
                issues.append("PILOT: incorrect local owner "+ident)
            if frm!=to and (root/frm).exists():
                issues.append("PILOT: legacy source not removed "+ident)
        elif item.get("ownership")=="external_companion":
            companion+=1
            if to!=frm or item.get("source_role")!="cross_program_companion_plan":
                issues.append("PILOT: companion cannot become second canonical source "+ident)
            if source.get("owner_programme")!="external" or any(
               source.get(key) is not None for key in
               ("source_repository","source_path","source_sha","source_url")):
                issues.append("PILOT: private source metadata not redacted "+ident)
        else:
            issues.append("PILOT: invalid owner mode "+ident)
        if frm!=to:
            rename+=1
    all_tex={p.relative_to(root).as_posix() for p in
             (root/"manuscripts").glob("*/main.tex")}
    if all_tex!=target_paths or seen!=set(byid):
        issues.append("PILOT: incomplete local sources or IDs")
    if len(public)!=27 or companion!=1 or rename!=6:
        issues.append("PILOT: counts drifted")
    return sorted(set(issues))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=ROOT)
    args=parser.parse_args()
    errors=audit(args.root)
    for err in errors:
        print("FAIL:",err)
    print("arc-v2-pilot-map:", "FAIL" if errors else "PASS",
          "; migration apply: NOT_RUN")
    return 1 if errors else 0


if __name__=="__main__":
    raise SystemExit(main())
