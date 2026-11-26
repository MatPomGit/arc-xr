"""Local Ollama benchmark runner; no ground truth is sent to the model."""
import argparse
import base64
import hashlib
import json
import time
from pathlib import Path
from urllib.request import Request, urlopen
from paired_eval import Trial, estimate

URL = 'http://127.0.0.1:11434'

def api(path, payload=None):
    data = None if payload is None else json.dumps(payload).encode()
    req = Request(URL + path, data=data, headers={'Content-Type':'application/json'})
    with urlopen(req, timeout=180) as response:
        return json.load(response)

def verified(root, name, digest):
    p = (root / name).resolve()
    if p.parent != root.resolve():
        raise ValueError('Unsafe fixture path')
    data = p.read_bytes()
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError('Fixture checksum mismatch')
    return data

def payload(model, image, prompt, geometry=None):
    text = prompt + '\nReply with exactly one letter A, B or C, or UNKNOWN.'
    if geometry is not None:
        text += '\nSpatial measurements: ' + geometry.decode('utf-8')
    return {'model':model,'stream':False,'messages':[{'role':'user','content':text,'images':[base64.b64encode(image).decode('ascii')]}], 'options':{'temperature':0,'seed':42,'num_predict':32}}

def run(root, out, model, split='development', limit=None, call=api):
    root, out = Path(root), Path(out)
    if out.exists(): raise FileExistsError(out)
    manifest = json.loads((root/'manifest.json').read_text(encoding='utf-8'))
    scenes = [s for s in manifest['scenes'] if s['split']==split]
    if limit is not None:
        if limit < 1: raise ValueError('limit must be positive')
        scenes = scenes[:limit]
    if not scenes: raise ValueError('No matching scenes')
    installed = call('/api/tags')
    matches = [m for m in installed['models'] if m.get('name') == model]
    if len(matches)!=1 or not matches[0].get('digest'): raise ValueError('Model not installed or digest missing; use exact name from ollama list')
    digest = matches[0]['digest']
    with out.open('x',encoding='utf-8') as f:
        for s in scenes:
            img = verified(root,s['rgb'],s['rgb_sha256'])
            geo = verified(root,s['geometry'],s['geometry_sha256'])
            for j,p in enumerate(s['prompts']):
                conditions = ['rgb','rgb3d'] if j%2==0 else ['rgb3d','rgb']
                for condition in conditions:
                    start=time.monotonic()
                    record={'scene':s['scene'],'prompt':p['id'],'condition':condition,'split':split,'limit':limit,'model':model,'model_digest':digest,'manifest_sha256':hashlib.sha256((root/'manifest.json').read_bytes()).hexdigest()}
                    try:
                        result=call('/api/chat',payload(model,img,p['text'],geo if condition=='rgb3d' else None))
                        raw=result['message']['content'].strip()
                        record.update(raw=raw, answer=raw if raw in ('A','B','C') else None,status='ok' if raw in ('A','B','C') else 'abstain' if raw=='UNKNOWN' else 'invalid_response')
                    except Exception as exc:
                        record.update(status='execution_error',answer=None,error=type(exc).__name__)
                    record['seconds']=time.monotonic()-start
                    f.write(json.dumps(record)+'\n'); f.flush()
                    print(s['scene'],p['id'],condition,record['status'],flush=True)

def score(root, log):
    root=Path(root)
    truth={(r['scene'],r['prompt']):r['target'] for r in json.loads((root/'ground_truth.json').read_text(encoding='utf-8'))}
    groups={}; metadata=set(); counts={}
    expected_hash=hashlib.sha256((root/'manifest.json').read_bytes()).hexdigest()
    for line in Path(log).read_text(encoding='utf-8').splitlines():
        r=json.loads(line); key=(r['scene'],r['prompt']); c=r['condition']
        if key not in truth or c not in ('rgb','rgb3d') or r['manifest_sha256']!=expected_hash: raise ValueError('Invalid record')
        if c in groups.setdefault(key,{}): raise ValueError('Duplicate condition')
        groups[key][c]=r; metadata.add((r['split'],r['model'],r['model_digest'],r['limit']))
        counts[r['status']]=counts.get(r['status'],0)+1
    if len(metadata)!=1: raise ValueError('Mixed or empty run')
    split, model, digest, limit = next(iter(metadata))
    manifest=json.loads((root/'manifest.json').read_text(encoding='utf-8'))
    selected=[s for s in manifest['scenes'] if s['split']==split]
    if limit is not None: selected=selected[:limit]
    expected={(s['scene'],p['id']) for s in selected for p in s['prompts']}
    if set(groups)!=expected: raise ValueError('Missing or unexpected paired prompts')
    trials=[]
    for key,g in groups.items():
        if set(g)!= {'rgb','rgb3d'} or any(r['status']=='execution_error' for r in g.values()): raise ValueError('Incomplete execution; no effect estimate')
        trials.append(Trial(*key,truth[key],g['rgb']['answer'],g['rgb3d']['answer']))
    return {'status_counts':counts,'split':split,'limit':limit,'model':model,'model_digest':digest, 'paired_prompts':len(trials),**estimate(trials)}

if __name__=='__main__':
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='command',required=True)
    r=sub.add_parser('run'); r.add_argument('root'); r.add_argument('out'); r.add_argument('--model',required=True); r.add_argument('--split',choices=['development','test'],default='development'); r.add_argument('--limit',type=int)
    s=sub.add_parser('score'); s.add_argument('root'); s.add_argument('log')
    a=p.parse_args()
    if a.command=='run': run(a.root,a.out,a.model,a.split,a.limit)
    else: print(json.dumps(score(a.root,a.log),indent=2))
