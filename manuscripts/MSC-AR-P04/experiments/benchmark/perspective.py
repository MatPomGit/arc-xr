"""Perspective cuboid fixtures for engineering validation, not real AR measurements."""
import argparse
import hashlib
import json
from pathlib import Path
from random import Random
from PIL import Image, ImageDraw

WIDTH, HEIGHT, FOCAL = 640, 480, 440

def project(x, y, z):
    if z <= 0:
        raise ValueError("Point behind camera")
    return (WIDTH / 2 + FOCAL * x / z, HEIGHT / 2 - FOCAL * y / z)

def faces(obj):
    x,z,w,h,d = (obj[k] for k in ("x_m","depth_m","width_m","height_m","length_m"))
    vertices = [(x+dx, y-0.65, z+dz) for dz in (-d/2,d/2) for y in (0,h) for dx in (-w/2,w/2)]
    indices = ((0,1,3,2),(4,5,7,6),(0,4,6,2),(1,5,7,3),(2,3,7,6),(0,1,5,4))
    shades = ("#527da0","#527da0","#365b78","#365b78","#8eafc5","#365b78")
    for idx,shade in zip(indices,shades):
        pts=[vertices[i] for i in idx]
        yield sum(p[2] for p in pts)/4, [project(*p) for p in pts], shade

def render(objects):
    image=Image.new("RGB",(WIDTH,HEIGHT),"#e7e8e5")
    draw=ImageDraw.Draw(image)
    draw.rectangle((0,HEIGHT//2,WIDTH,HEIGHT),fill="#c9c8c0")
    # Objects occupy disjoint image columns; painter ordering is sufficient here.
    polygons=[face for obj in objects for face in faces(obj)]
    for _,points,shade in sorted(polygons,key=lambda f:-f[0]):
        draw.polygon(points,fill=shade,outline="#253747")
    for obj in objects:
        x,y=project(obj["x_m"],obj["height_m"]-0.65,obj["depth_m"])
        draw.text((x-4,y-15),obj["id"],fill="#111111")
    return image

def generate(root, seed=42, n=30):
    if type(n) is not int or not 6 <= n <= 3000:
        raise ValueError("n must be an integer from 6 to 3000")
    root=Path(root)
    root.mkdir(parents=True,exist_ok=False)
    rng=Random(seed)
    layouts=set()
    scenes,truth=[],[]
    for i in range(n):
        while True:
            # Distinct distances and heights prevent ties; projected centres fixed apart.
            depths=rng.sample(range(25,46),3)
            heights=rng.sample(range(4,13),3)
            key=tuple(zip(depths,heights))
            if key not in layouts:
                layouts.add(key)
                break
        ids=rng.sample(["A","B","C"],3)
        objects=[]
        for label,offset,depth,height in zip(ids,(-155,0,155),depths,heights):
            z=depth/10
            objects.append(dict(id=label,x_m=round(offset*z/FOCAL,8),depth_m=z,
                                height_m=height/10,width_m=0.36,length_m=0.30))
        sid=f"p{i:05d}"
        rgb=root/(sid+".png")
        geo=root/(sid+".geometry.json")
        render(objects).save(rgb)
        geometry={"frame":"camera-aligned, x right, y up, depth positive away from camera; floor y=-0.65 m",
                  "camera":{"projection":"pinhole","fx_px":FOCAL,"fy_px":FOCAL,"cx_px":WIDTH/2,"cy_px":HEIGHT/2},
                  "objects":objects}
        geo.write_text(json.dumps(geometry,sort_keys=True),encoding="utf-8")
        prompts=[("near","Which object is nearest to the camera?",min(objects,key=lambda o:o["depth_m"])),
                 ("high","Which object has the greatest physical height?",max(objects,key=lambda o:o["height_m"]))]
        scenes.append({"scene":sid,"split":"development" if i<n//3 else "test","rgb":rgb.name,"geometry":geo.name,
                       "rgb_sha256":hashlib.sha256(rgb.read_bytes()).hexdigest(),
                       "geometry_sha256":hashlib.sha256(geo.read_bytes()).hexdigest(),
                       "prompts":[{"id":k,"text":p} for k,p,_ in prompts]})
        truth.extend({"scene":sid,"prompt":k,"target":o["id"]} for k,_,o in prompts)
    (root/"manifest.json").write_text(json.dumps({"version":"0.2.0","fixture":"perspective_cuboids","seed":seed,"scenes":scenes},indent=2),encoding="utf-8")
    (root/"ground_truth.json").write_text(json.dumps(truth,indent=2),encoding="utf-8")

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("output")
    p.add_argument("--seed",type=int,default=42)
    p.add_argument("--n",type=int,default=30)
    a=p.parse_args()
    generate(a.output,a.seed,a.n)
