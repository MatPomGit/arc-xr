"""Exploratory matched-scene robustness matrix; no automatic test-set execution."""
import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from random import Random
from statistics import mean
from perturbations import generate
from run_vlm import run

LEVELS = [(s,o) for o in (0,10,25) for s in (0,2,5)]
def cell(s,o):
    return f"s{s:02d}_o{o:02d}"

def prepare(source, output, seed=42):
    output=Path(output)
    output.mkdir(parents=True,exist_ok=False)
    for s,o in LEVELS:
        generate(source,output/cell(s,o),s/100,o/100,seed)

def execute(root, model, limit=2):
    if type(limit) is not int or limit<2:
        raise ValueError("At least two development scenes required")
    root=Path(root)
    for s,o in LEVELS:
        path=root/cell(s,o)
        run(path,path/"pilot.jsonl",model,split="development",limit=limit)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def read_cell(path,s,o):
    raw=(path/"manifest.json").read_bytes()
    m=json.loads(raw)
    t_raw=(path/"ground_truth.json").read_bytes()
    if m.get("fixture")!="perspective_perturbed" or m["ground_truth_sha256"]!=sha(t_raw):
        raise ValueError("Reference integrity mismatch")
    params=m["perturbation"]
    if (params["sigma_m"],params["image_band_fraction"])!=(s/100,o/100):
        raise ValueError("Incorrect cell parameters")
    truth={}
    for t in json.loads(t_raw):
        k=t["scene"],t["prompt"]
        if k in truth or t["target"] not in ("A","B","C"):
            raise ValueError("Invalid reference")
        truth[k]=t["target"]
    metadata=set(); records={}
    for line in (path/"pilot.jsonl").read_text(encoding="utf-8").splitlines():
        r=json.loads(line)
        key=r["scene"],r["prompt"],r["condition"]
        if key in records or r["manifest_sha256"]!=sha(raw) or r["condition"] not in ("rgb","rgb3d"):
            raise ValueError("Duplicate or incompatible result")
        status,answer=r["status"],r["answer"]
        if not ((status=="ok" and answer in ("A","B","C")) or (status in ("abstain","invalid_response") and answer is None)):
            raise ValueError("Incomplete or inconsistent execution")
        metadata.add((r["model"],r["model_digest"],r["split"],r["limit"]))
        records[key]=int(answer==truth[key[:2]])
    if len(metadata)!=1:
        raise ValueError("Mixed execution metadata")
    model,digest,split,limit=next(iter(metadata))
    if split!="development" or type(limit) is not int or limit<2 or not model or not digest:
        raise ValueError("Development-only matrix required")
    scenes=[x for x in m["scenes"] if x["split"]==split][:limit]
    expected={(x["scene"],p["id"],c) for x in scenes for p in x["prompts"] for c in ("rgb","rgb3d")}
    if set(records)!=expected or len(scenes)<2:
        raise ValueError("Missing or unexpected observations")
    values={}
    for x in scenes:
        sid=x["scene"]
        if sid in values or not x["prompts"]:
            raise ValueError("Invalid scene")
        values[sid]=tuple(mean(records[sid,p["id"],c] for p in x["prompts"]) for c in ("rgb","rgb3d"))
    signature=(model,digest,split,limit,m["source_manifest_sha256"],m["ground_truth_sha256"],params["seed"],tuple(sorted(expected)))
    return signature,values

def interval(values,seed=42,replicates=2000):
    if len(values)<2 or replicates<100:
        raise ValueError("Insufficient scenes or replicates")
    rng=Random(seed); n=len(values)
    draws=sorted(mean(rng.choices(values,k=n)) for _ in range(replicates))
    return mean(values),draws[int(.025*(replicates-1))],draws[int(.975*(replicates-1))]

def analyze(root):
    root=Path(root); signature=None; data={}
    for s,o in LEVELS:
        sig,values=read_cell(root/cell(s,o),s,o)
        if signature is not None and sig!=signature:
            raise ValueError("Matrix cells do not share model, references and paired trials")
        signature=sig; data[s,o]=values
    ids=sorted(data[0,0])
    rows=[]
    for s,o in LEVELS:
        pairs=data[s,o]
        d=[pairs[i][1]-pairs[i][0] for i in ids]
        gain,lo,hi=interval(d)
        # Difference-in-differences of the geometry advantage on matched scenes.
        interaction=[(pairs[i][1]-pairs[i][0])-(data[s,0][i][1]-data[s,0][i][0])-(data[0,o][i][1]-data[0,o][i][0])+(data[0,0][i][1]-data[0,0][i][0]) for i in ids]
        effect,il,ih=interval(interaction)
        rows.append(dict(sigma_cm=s,occlusion_pct=o,n_scenes=len(ids),
                         rgb_accuracy=mean(pairs[i][0] for i in ids),
                         rgb3d_accuracy=mean(pairs[i][1] for i in ids),
                         gain=gain,gain_lo=lo,gain_hi=hi,interaction=effect,
                         interaction_lo=il,interaction_hi=ih))
    return rows

def report(root,output):
    rows=analyze(root)
    with Path(output).open("x",encoding="utf-8",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)

if __name__=="__main__":
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True)
    a=sub.add_parser("prepare"); a.add_argument("source"); a.add_argument("root"); a.add_argument("--seed",type=int,default=42)
    a=sub.add_parser("run"); a.add_argument("root"); a.add_argument("--model",required=True); a.add_argument("--limit",type=int,default=2)
    a=sub.add_parser("report"); a.add_argument("root"); a.add_argument("output")
    a=p.parse_args()
    if a.cmd=="prepare": prepare(a.source,a.root,a.seed)
    elif a.cmd=="run": execute(a.root,a.model,a.limit)
    else: report(a.root,a.output)
