"""Deterministic geometry-only diagnostic baseline for fixed prompt templates."""
import argparse
import hashlib
import json
import math
import time
from pathlib import Path
from statistics import mean

def predict(geometry, prompt):
    objects=geometry["objects"]
    if len(objects)!=3 or {o["id"] for o in objects}!={"A","B","C"}:
        raise ValueError("Invalid candidate identities")
    rules={
        "near":("depth_m",1),
        "high":("height_m",-1),
    }
    if prompt not in rules:
        raise ValueError("Unsupported prompt template")
    key,sign=rules[prompt]
    values=[]
    for obj in objects:
        v=obj[key]
        if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<=0:
            raise ValueError("Invalid measurement")
        values.append((sign*v,obj["id"]))
    values.sort()
    if math.isclose(values[0][0],values[1][0],rel_tol=0,abs_tol=1e-8):
        return None
    return values[0][1]

def evaluate(root, output, limit=2):
    root,output=Path(root),Path(output)
    if type(limit) is not int or limit<2:
        raise ValueError("At least two scenes required")
    raw=(root/"manifest.json").read_bytes()
    m=json.loads(raw)
    if m.get("fixture") not in ("perspective_cuboids","perspective_perturbed"):
        raise ValueError("Unsupported fixture")
    truth_raw=(root/"ground_truth.json").read_bytes()
    if m.get("ground_truth_sha256",hashlib.sha256(truth_raw).hexdigest())!=hashlib.sha256(truth_raw).hexdigest():
        raise ValueError("Reference checksum mismatch")
    truth={}
    for t in json.loads(truth_raw):
        k=t["scene"],t["prompt"]
        if k in truth or t["target"] not in ("A","B","C"):
            raise ValueError("Invalid ground truth")
        truth[k]=t["target"]
    scenes=[s for s in m["scenes"] if s["split"]=="development"][:limit]
    if len(scenes)<2 or len({s["scene"] for s in scenes})!=len(scenes):
        raise ValueError("Insufficient independent scenes")
    rows=[]; accuracy=[]
    for scene in scenes:
        path=(root/scene["geometry"]).resolve()
        if path.parent!=root.resolve():
            raise ValueError("Unsafe path")
        data=path.read_bytes()
        if hashlib.sha256(data).hexdigest()!=scene["geometry_sha256"]:
            raise ValueError("Geometry checksum mismatch")
        geometry=json.loads(data)
        scores=[]; seen=set()
        for p in scene["prompts"]:
            key=scene["scene"],p["id"]
            if key in seen or key not in truth:
                raise ValueError("Invalid prompt identity")
            seen.add(key)
            start=time.perf_counter_ns()
            answer=predict(geometry,p["id"])
            elapsed=time.perf_counter_ns()-start
            correct=int(answer==truth[key])
            scores.append(correct)
            rows.append(dict(scene=key[0],prompt=key[1],answer=answer,correct=correct,compute_ns=elapsed))
        if not scores:
            raise ValueError("Empty scene")
        accuracy.append(mean(scores))
    result=dict(method="geometry_only_template",split="development",n_scenes=len(scenes),
                accuracy=mean(accuracy),manifest_sha256=hashlib.sha256(raw).hexdigest(),
                truth_sha256=hashlib.sha256(truth_raw).hexdigest(),trials=rows)
    with output.open("x",encoding="utf-8") as f:
        json.dump(result,f,indent=2)
    return result

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("root");p.add_argument("output");p.add_argument("--limit",type=int,default=2)
    a=p.parse_args()
    print(json.dumps(evaluate(a.root,a.output,a.limit),indent=2))
