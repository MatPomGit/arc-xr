import json
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree
from geometry_baseline import predict, evaluate
from perspective import generate
from export_report import export
from test_robustness import fixture

class BaselineTest(unittest.TestCase):
    def geometry(self):
        return {"objects":[{"id":"A","depth_m":2,"height_m":.5},
                           {"id":"B","depth_m":3,"height_m":.8},
                           {"id":"C","depth_m":4,"height_m":.6}]}

    def test_rules_and_order(self):
        g=self.geometry()
        self.assertEqual(predict(g,"near"),"A")
        self.assertEqual(predict(g,"high"),"B")
        g["objects"].reverse()
        self.assertEqual(predict(g,"near"),"A")

    def test_tie(self):
        g=self.geometry()
        g["objects"][1]["depth_m"]=2
        self.assertIsNone(predict(g,"near"))

    def test_invalid(self):
        for v in (0,-1,float("nan"),float("inf"),True,"2"):
            g=self.geometry()
            g["objects"][0]["depth_m"]=v
            with self.assertRaises(ValueError):
                predict(g,"near")
        with self.assertRaises(ValueError):
            predict(self.geometry(),"other")
        g=self.geometry()
        g["objects"][1]["id"]="A"
        with self.assertRaises(ValueError):
            predict(g,"near")

    def test_clean_fixture(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/"data"; out=Path(d)/"baseline.json"
            generate(root,n=6)
            result=evaluate(root,out)
            self.assertEqual(result["accuracy"],1)
            self.assertEqual(result["n_scenes"],2)
            self.assertEqual(len(result["trials"]),4)
            self.assertEqual(json.loads(out.read_text()),result)
            with self.assertRaises(FileExistsError):
                evaluate(root,out)

    def test_integrity(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/"data"; generate(root,n=6)
            (root/"p00000.geometry.json").write_text("{}")
            with self.assertRaises(ValueError):
                evaluate(root,Path(d)/"baseline.json")

class ExportTest(unittest.TestCase):
    def test_export(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); matrix=fixture(root); out=root/"report"
            export(matrix,out)
            report=json.loads((out/"report.json").read_text())
            self.assertEqual(report["scope"],"exploratory_development")
            self.assertEqual(len(report["rows"]),9)
            self.assertEqual(len(report["inputs_sha256"]),27)
            self.assertEqual(ElementTree.parse(out/"robustness.svg").getroot().tag,"{http://www.w3.org/2000/svg}svg")
            tex=(out/"robustness_table.tex").read_text()
            self.assertEqual(tex.count("\\\\"),10)
            self.assertIn(r"\end{tabular}",tex)
            with self.assertRaises(FileExistsError):
                export(matrix,out)

    def test_incomplete(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); matrix=fixture(root)
            (matrix/"s00_o00"/"pilot.jsonl").unlink()
            with self.assertRaises(FileNotFoundError):
                export(matrix,root/"report")
            self.assertFalse((root/"report").exists())

if __name__=="__main__":
    unittest.main()
