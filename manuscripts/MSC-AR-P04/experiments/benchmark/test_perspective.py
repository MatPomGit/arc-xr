import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from PIL import Image
from perspective import generate, project, WIDTH, HEIGHT, FOCAL

class PerspectiveTest(unittest.TestCase):
    def test_projection(self):
        self.assertEqual(project(0,0,2),(WIDTH/2,HEIGHT/2))
        self.assertAlmostEqual(project(1,0,2)[0]-WIDTH/2,FOCAL/2)
        with self.assertRaises(ValueError):
            project(0,0,0)

    def test_ground_truth_and_integrity(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/"fixtures"
            generate(root,n=30)
            manifest=json.loads((root/"manifest.json").read_text())
            truth=json.loads((root/"ground_truth.json").read_text())
            self.assertEqual(len(manifest["scenes"]),30)
            self.assertEqual(len(truth),60)
            self.assertEqual(sum(s["split"]=="test" for s in manifest["scenes"]),20)
            labels={(r["scene"],r["prompt"]):r["target"] for r in truth}
            layouts=set()
            for s in manifest["scenes"]:
                geo=json.loads((root/s["geometry"]).read_text())
                objects=geo["objects"]
                key=tuple((o["depth_m"],o["height_m"]) for o in objects)
                self.assertNotIn(key,layouts)
                layouts.add(key)
                self.assertEqual(labels[s["scene"],"near"],min(objects,key=lambda o:o["depth_m"])["id"])
                self.assertEqual(labels[s["scene"],"high"],max(objects,key=lambda o:o["height_m"])["id"])
                self.assertNotIn("target",json.dumps(geo))
                self.assertNotIn("target",json.dumps(s))
                for kind in ("rgb","geometry"):
                    self.assertEqual(hashlib.sha256((root/s[kind]).read_bytes()).hexdigest(),s[kind+"_sha256"])
                with Image.open(root/s["rgb"]) as im:
                    self.assertEqual(im.size,(WIDTH,HEIGHT))

    def test_reproducibility(self):
        with tempfile.TemporaryDirectory() as d:
            a,b=Path(d)/"a",Path(d)/"b"
            generate(a,seed=12,n=6)
            generate(b,seed=12,n=6)
            self.assertEqual({p.name:p.read_bytes() for p in a.iterdir()},
                             {p.name:p.read_bytes() for p in b.iterdir()})

    def test_bounds(self):
        for n in (0,5,3001,True,6.0):
            with self.assertRaises(ValueError):
                generate("unused",n=n)

if __name__=="__main__":
    unittest.main()
