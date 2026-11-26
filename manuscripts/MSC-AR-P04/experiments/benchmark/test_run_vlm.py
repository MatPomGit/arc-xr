import json
import tempfile
import unittest
from pathlib import Path
from scenes import generate
from run_vlm import run,score,payload

class AdapterTest(unittest.TestCase):
    def test_isolation(self):
        a=payload('m',b'image','question'); b=payload('m',b'image','question',b'{"z":2}')
        self.assertNotIn('Spatial measurements',a['messages'][0]['content'])
        self.assertIn('{"z":2}',b['messages'][0]['content'])
        self.assertEqual(a['messages'][0]['images'],b['messages'][0]['images'])
    def test_mock_run_and_score(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'data'; log=Path(d)/'log'; generate(root,n=6)
            def fake(path,p=None):
                if path=='/api/tags': return {'models':[{'name':'m','digest':'abc'}]}
                return {'message':{'content':'A'}}
            run(root,log,'m',call=fake)
            result=score(root,log); self.assertEqual(result['difference'],0); self.assertEqual(result['paired_prompts'],4)
            lines=log.read_text().splitlines(); log.write_text('\n'.join(lines[:-2]))
            with self.assertRaises(ValueError): score(root,log)
            with self.assertRaises(FileExistsError): run(root,log,'m',call=fake)
    def test_failed_execution(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'data'; log=Path(d)/'log'; generate(root,n=6)
            def fake(path,p=None):
                if path=='/api/tags': return {'models':[{'name':'m','digest':'abc'}]}
                raise TimeoutError()
            run(root,log,'m',call=fake)
            with self.assertRaises(ValueError): score(root,log)
    def test_checksum(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d)/'data'; generate(root,n=6); (root/'s00000.png').write_bytes(b'bad')
            with self.assertRaises(ValueError): run(root,Path(d)/'log','m',call=lambda *a:{'models':[{'name':'m','digest':'abc'}]})
if __name__=='__main__': unittest.main()
