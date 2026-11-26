import unittest
from paired_eval import Trial, estimate, scene_differences

class TestPairedEval(unittest.TestCase):
    def test_equal_scene_weight(self):
        rows = [Trial('a', str(i), 'x', 'y', 'x') for i in range(10)] + [Trial('b','1','x','x','y')]
        self.assertEqual(estimate(rows, replicates=100)['difference'], 0)
    def test_abstention(self):
        self.assertEqual(scene_differences([Trial('a','1','x',None,'x')]), {'a':1})
    def test_duplicates(self):
        t=Trial('a','1','x','x','x')
        with self.assertRaises(ValueError): scene_differences([t,t])
    def test_empty(self):
        with self.assertRaises(ValueError): scene_differences([])
    def test_single_scene(self):
        with self.assertRaises(ValueError): estimate([Trial('a','1','x','x','x')])
    def test_determinism(self):
        rows=[Trial('a','1','x','y','x'),Trial('b','1','x','x','x')]
        self.assertEqual(estimate(rows,replicates=100),estimate(rows[::-1],replicates=100))
    def test_missing_target(self):
        with self.assertRaises(ValueError): scene_differences([Trial('a','1','',None,None)])

if __name__ == '__main__': unittest.main()
