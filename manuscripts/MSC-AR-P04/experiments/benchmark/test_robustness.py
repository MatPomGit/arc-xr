import csv
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from perspective import generate
from robustness import LEVELS, cell, prepare, execute, analyze, report, interval, sha

def fixture(root):
    source=root/"source"; matrix=root/"matrix"
    generate(source,n=6); prepare(source,matrix)
    for s,o in LEVELS:
        path=matrix/cell(s,o)
        raw=(path/"manifest.json").read_bytes()
        manifest=json.loads(raw)
        truth={(t["scene"],t["prompt"]):t["target"] for t in json.loads((path/"ground_truth.json").read_bytes())}
        records=[]
        for scene in [x for x in manifest["scenes"] if x["split"]=="development"]:
            for prompt in scene["prompts"]:
                target=truth[scene["scene"],prompt["id"]]
                wrong=next(x for x in "ABC" if x!=target)
                for condition in ("rgb","rgb3d"):
                    answer=target if condition=="rgb3d" and (s==0 or o==0) else wrong
                    records.append(dict(scene=scene["scene"],prompt=prompt["id"],condition=condition,
                                        model="mock",model_digest="fixed",split="development",limit=2,
                                        manifest_sha256=sha(raw),status="ok",answer=answer))
        (path/"pilot.jsonl").write_text("\n".join(map(json.dumps,records)),encoding="utf-8")
    return matrix

class RobustnessTest(unittest.TestCase):
    def test_known_interaction(self):
        with tempfile.TemporaryDirectory() as d:
            matrix=fixture(Path(d)); rows=analyze(matrix)
            self.assertEqual(len(rows),9)
            for row in rows:
                both=row["sigma_cm"]>0 and row["occlusion_pct"]>0
                self.assertEqual(row["gain"],0 if both else 1)
                self.assertEqual(row["interaction"],-1 if both else 0)
                self.assertEqual(row["n_scenes"],2)
            out=Path(d)/"report.csv"; report(matrix,out)
            with out.open(newline="") as f: self.assertEqual(len(list(csv.DictReader(f))),9)
            with self.assertRaises(FileExistsError): report(matrix,out)

    def test_missing_and_duplicate(self):
        with tempfile.TemporaryDirectory() as d:
            matrix=fixture(Path(d)); p=matrix/cell(0,0)/"pilot.jsonl"
            lines=p.read_text().splitlines()
            for altered in (lines[:-1],lines+[lines[0]]):
                p.write_text("\n".join(altered))
                with self.assertRaises(ValueError): analyze(matrix)

    def test_model_and_reference_mismatch(self):
        with tempfile.TemporaryDirectory() as d:
            matrix=fixture(Path(d)); p=matrix/cell(5,25)/"pilot.jsonl"
            lines=[json.loads(x) for x in p.read_text().splitlines()]
            for r in lines: r["model_digest"]="changed"
            p.write_text("\n".join(map(json.dumps,lines)))
            with self.assertRaises(ValueError): analyze(matrix)
            t=matrix/cell(0,0)/"ground_truth.json"
            t.write_bytes(t.read_bytes()+b" ")
            with self.assertRaises(ValueError): analyze(matrix)

    def test_execution_failure(self):
        with tempfile.TemporaryDirectory() as d:
            matrix=fixture(Path(d)); p=matrix/cell(0,0)/"pilot.jsonl"
            lines=[json.loads(x) for x in p.read_text().splitlines()]
            lines[0].update(status="execution_error",answer=None)
            p.write_text("\n".join(map(json.dumps,lines)))
            with self.assertRaises(ValueError): analyze(matrix)

    def test_development_only(self):
        with patch("robustness.run") as run:
            execute("unused","mock",2)
            self.assertEqual(run.call_count,9)
            self.assertTrue(all(c.kwargs["split"]=="development" for c in run.call_args_list))
        with self.assertRaises(ValueError): execute("unused","mock",1)

    def test_interval(self):
        self.assertEqual(interval([1,1]),(1,1,1))
        self.assertEqual(interval([-1,1]),interval([-1,1]))
        with self.assertRaises(ValueError): interval([1])

if __name__=="__main__":
    unittest.main()
