import json, tempfile, unittest, hashlib
from pathlib import Path
from scenes import generate
from PIL import Image

class ScenesTest(unittest.TestCase):
    def test_contract(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'a'; generate(root,42,30)
            m=json.loads((root/'manifest.json').read_text())['scenes']; t=json.loads((root/'ground_truth.json').read_text()); self.assertEqual(len(m),30); self.assertEqual(len(t),60)
            self.assertEqual(sum(s['split']=='test' for s in m),20)
            layouts=set()
            for s in m:
                g=json.loads((root/s['geometry']).read_text())['objects']; key=tuple(sorted((o['x_px'],o['y_px'],o['z_m']) for o in g)); self.assertNotIn(key,layouts); layouts.add(key)
                self.assertEqual({o['id'] for o in g},{'A','B','C'}); self.assertNotIn('target',json.dumps(s)); self.assertNotIn('target',json.dumps(g))
                self.assertEqual(hashlib.sha256((root/s['rgb']).read_bytes()).hexdigest(),s['rgb_sha256']); self.assertEqual(hashlib.sha256((root/s['geometry']).read_bytes()).hexdigest(),s['geometry_sha256'])
                with Image.open(root/s['rgb']) as im: self.assertEqual(im.size,(320,260))
                targets={x['prompt']:x['target'] for x in t if x['scene']==s['scene']}; self.assertEqual(targets['left'],min(g,key=lambda o:o['x_px'])['id']); self.assertEqual(targets['high'],max(g,key=lambda o:o['z_m'])['id'])
    def test_reproducibility(self):
        with tempfile.TemporaryDirectory() as d:
            a,b=Path(d)/'a',Path(d)/'b'; generate(a);generate(b)
            self.assertEqual({p.name:p.read_bytes() for p in a.iterdir()},{p.name:p.read_bytes() for p in b.iterdir()})
    def test_invalid_n(self):
        with self.assertRaises(ValueError): generate('unused',n=5)
    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(FileExistsError): generate(d)
if __name__=='__main__': unittest.main()
