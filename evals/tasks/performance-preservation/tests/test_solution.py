import unittest
from stats import unique_stable
class Key:
    comparisons=0
    def __init__(self,n):self.n=n
    def __hash__(self):return hash(self.n)
    def __eq__(self,other):
        Key.comparisons+=1
        return isinstance(other,Key) and self.n==other.n
class Tests(unittest.TestCase):
    def test_order(self):
        self.assertEqual(unique_stable(['b','a','b','c','a']),['b','a','c'])
    def test_unhashable(self):
        self.assertEqual(unique_stable([[1],[1],[2],[1]]),[[1],[2]])
    def test_mixed(self):
        self.assertEqual(unique_stable([1,[1],1,[1],2]),[1,[1],2])
    def test_return_type(self):
        self.assertIsInstance(unique_stable((1,1,2)),list)
    def test_comparison_budget(self):
        Key.comparisons=0
        values=[Key(i) for i in range(250)]
        self.assertEqual([x.n for x in unique_stable(values)],list(range(250)))
        self.assertLess(Key.comparisons,2000,'Hashable inputs should avoid quadratic equality comparisons')
