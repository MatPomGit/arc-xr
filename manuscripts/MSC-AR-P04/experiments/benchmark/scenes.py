"""Synthetic orthographic grounding fixtures; no model inference or real calibration."""
import argparse
import hashlib
import json
from pathlib import Path
from random import Random
from PIL import Image, ImageDraw

def generate(root, seed=42, n=30):
    if type(n) is not int or n < 6:
        raise ValueError('At least six scenes required')
    root = Path(root)
    root.mkdir(parents=True, exist_ok=False)
    rng = Random(seed)
    layouts = set()
    manifest, truth = [], []
    for i in range(n):
        sid = f's{i:05d}'
        # Orthographic top view: x/y in pixels, z in metres, not visible in RGB.
        while True:
            xy = tuple((x, rng.randrange(50, 210)) for x in rng.sample(range(40, 281, 80), 3))
            z = tuple(rng.sample(range(1, 21), 3))
            key = tuple(sorted(zip(xy, z)))
            if key not in layouts:
                layouts.add(key)
                break
        ids = rng.sample(['A', 'B', 'C'], 3)
        objects = [dict(id=k, x_px=x, y_px=y, z_m=h/10) for k,(x,y),h in zip(ids,xy,z)]
        img = Image.new('RGB', (320, 260), 'white')
        draw = ImageDraw.Draw(img)
        for obj in objects:
            x,y = obj['x_px'],obj['y_px']
            draw.rectangle((x-18,y-18,x+18,y+18), fill='#4477aa', outline='black')
            draw.text((x-3,y-5),obj['id'],fill='white')
        image_path = root / (sid+'.png')
        img.save(image_path)
        geometry = {'frame':'synthetic orthographic image; z upward in metres', 'objects':objects}
        geo_path = root / (sid+'.geometry.json')
        geo_path.write_text(json.dumps(geometry, sort_keys=True), encoding='utf-8')
        prompts = [('left','Which object is leftmost? Return A, B or C.',min(objects,key=lambda o:o['x_px'])),('high','Which object has the greatest height (z)? Return A, B or C.',max(objects,key=lambda o:o['z_m']))]
        manifest.append({'scene':sid,'split':'development' if i < n//3 else 'test','rgb':image_path.name,'geometry':geo_path.name,'prompts':[{'id':k,'text':p} for k,p,_ in prompts], 'rgb_sha256':hashlib.sha256(image_path.read_bytes()).hexdigest(),'geometry_sha256':hashlib.sha256(geo_path.read_bytes()).hexdigest()})
        truth.extend({'scene':sid,'prompt':k,'target':o['id']} for k,_,o in prompts)
    (root/'manifest.json').write_text(json.dumps({'version':'0.1.0','seed':seed,'scenes':manifest},indent=2),encoding='utf-8')
    (root/'ground_truth.json').write_text(json.dumps(truth,indent=2),encoding='utf-8')

if __name__ == '__main__':
    p=argparse.ArgumentParser(); p.add_argument('output'); p.add_argument('--seed',type=int,default=42); p.add_argument('--n',type=int,default=30)
    a=p.parse_args(); generate(a.output,a.seed,a.n)
