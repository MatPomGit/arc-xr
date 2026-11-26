"""Paired synthetic perturbations of perspective fixtures; preserve reference labels."""
import argparse
import hashlib
import json
import math
from pathlib import Path
from random import Random
from PIL import Image, ImageDraw

def digest(data):
    return hashlib.sha256(data).hexdigest()

def verified(root, name, expected):
    path=(root/name).resolve()
    if path.parent != root.resolve():
        raise ValueError("Unsafe fixture path")
    data=path.read_bytes()
    if digest(data)!=expected:
        raise ValueError("Checksum mismatch")
    return data

def perturb_geometry(geometry, sigma, rng):
    if not math.isfinite(sigma) or not 0 <= sigma <= 0.1:
        raise ValueError("sigma must be between 0 and 0.1 m")
    copy=json.loads(json.dumps(geometry))
    for obj in copy["objects"]:
        for key in ("x_m","depth_m","height_m"):
            value=obj[key]+rng.gauss(0,sigma) if sigma else obj[key]
            if key!="x_m" and value<=0:
                raise ValueError("Nonpositive perturbed dimension")
            obj[key]=round(value,8) if sigma else value
    return copy

def occlude(image, fraction, rng):
    """Image-plane occluder, not physical inter-object occlusion."""
    if not math.isfinite(fraction) or not 0 <= fraction <= 0.4:
        raise ValueError("fraction must be between 0 and 0.4")
    result=image.copy()
    if fraction:
        w,h=result.size
        width=max(1,round(w*fraction))
        # Central vertical band, with randomized horizontal position.
        left=rng.randint(w//4, 3*w//4-width)
        ImageDraw.Draw(result).rectangle((left,0,left+width-1,h-1),fill="#777777")
    return result

def generate(source, output, sigma=0.0, fraction=0.0, seed=42):
    source,output=Path(source),Path(output)
    if not math.isfinite(sigma) or not 0<=sigma<=0.1 or not math.isfinite(fraction) or not 0<=fraction<=0.4:
        raise ValueError("Invalid perturbation levels")
    raw=(source/"manifest.json").read_bytes()
    manifest=json.loads(raw)
    if manifest.get("fixture")!="perspective_cuboids":
        raise ValueError("Expected unperturbed perspective fixtures")
    truth=(source/"ground_truth.json").read_bytes()
    output.mkdir(parents=True,exist_ok=False)
    scenes=[]
    for scene in manifest["scenes"]:
        sid=scene["scene"]
        # Independent streams keep noise and occluder placement factorially matched.
        rng_geo=Random(f"{seed}:{sid}:geometry")
        rng_rgb=Random(f"{seed}:{sid}:rgb")
        rgb=verified(source,scene["rgb"],scene["rgb_sha256"])
        geo=verified(source,scene["geometry"],scene["geometry_sha256"])
        import io
        with Image.open(io.BytesIO(rgb)) as image:
            transformed=occlude(image.convert("RGB"),fraction,rng_rgb)
        row=dict(scene)
        (output/row["rgb"]).write_bytes(rgb) if not fraction else transformed.save(output/row["rgb"])
        altered=perturb_geometry(json.loads(geo),sigma,rng_geo)
        (output/row["geometry"]).write_bytes(geo if not sigma else json.dumps(altered,sort_keys=True).encode())
        for kind in ("rgb","geometry"):
            row[kind+"_sha256"]=digest((output/row[kind]).read_bytes())
        scenes.append(row)
    result=dict(manifest,version="0.3.0",fixture="perspective_perturbed",scenes=scenes,
                perturbation={"sigma_m":sigma,"image_band_fraction":fraction,"seed":seed},
                source_manifest_sha256=digest(raw),ground_truth_sha256=digest(truth))
    (output/"manifest.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    (output/"ground_truth.json").write_bytes(truth)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("source"); p.add_argument("output")
    p.add_argument("--sigma",type=float,default=0.0)
    p.add_argument("--fraction",type=float,default=0.0)
    p.add_argument("--seed",type=int,default=42)
    a=p.parse_args()
    generate(a.source,a.output,a.sigma,a.fraction,a.seed)
