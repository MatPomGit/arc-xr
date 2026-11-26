import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from random import Random
from PIL import Image
from perspective import generate as perspective
from perturbations import generate, perturb_geometry, occlude

class PerturbationTest(unittest.TestCase):
    def test_identity_and_truth(self):
        with tempfile.TemporaryDirectory() as d:
            src,out=Path(d)/"src",Path(d)/"out"
            perspective(src,n=6)
            generate(src,out)
            m=json.loads((src/"manifest.json").read_text())
            n=json.loads((out/"manifest.json").read_text())
            self.assertEqual(m["scenes"],n["scenes"])
            self.assertEqual((src/"ground_truth.json").read_bytes(),(out/"ground_truth.json").read_bytes())

    def test_factorial_independence(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); src=root/"src"; perspective(src,n=6)
            for name,sigma,f in (("g",.02,0),("o",0,.1),("both",.02,.1),("rep",.02,.1)):
                generate(src,root/name,sigma,f)
            for scene in json.loads((src/"manifest.json").read_text())["scenes"]:
                rgb,geo=scene["rgb"],scene["geometry"]
                self.assertEqual((root/"g"/geo).read_bytes(),(root/"both"/geo).read_bytes())
                self.assertEqual((root/"o"/rgb).read_bytes(),(root/"both"/rgb).read_bytes())
                self.assertEqual((src/rgb).read_bytes(),(root/"g"/rgb).read_bytes())
                self.assertEqual((src/geo).read_bytes(),(root/"o"/geo).read_bytes())
            self.assertEqual({p.name:p.read_bytes() for p in (root/"both").iterdir()},
                             {p.name:p.read_bytes() for p in (root/"rep").iterdir()})
            m=json.loads((root/"both"/"manifest.json").read_text())
            for scene in m["scenes"]:
                for k in ("rgb","geometry"):
                    self.assertEqual(hashlib.sha256((root/"both"/scene[k]).read_bytes()).hexdigest(),scene[k+"_sha256"])
            self.assertEqual(m["ground_truth_sha256"],hashlib.sha256((src/"ground_truth.json").read_bytes()).hexdigest())

    def test_band_area(self):
        image=Image.new("RGB",(640,480),"white")
        result=occlude(image,.25,Random(1))
        count=sum(p==(119,119,119) for p in result.getdata())
        self.assertEqual(count,160*480)

    def test_invalid_parameters(self):
        for v in (-.01,float("nan"),float("inf"),.11):
            with self.assertRaises(ValueError):
                perturb_geometry({},v,Random(1))
        for v in (-.01,.41,float("nan")):
            with self.assertRaises(ValueError):
                occlude(Image.new("RGB",(640,480)),v,Random(1))

    def test_corrupted_input(self):
        with tempfile.TemporaryDirectory() as d:
            src,out=Path(d)/"src",Path(d)/"out"
            perspective(src,n=6)
            (src/"p00000.png").write_bytes(b"corrupted")
            with self.assertRaises(ValueError):
                generate(src,out)

if __name__=="__main__":
    unittest.main()
