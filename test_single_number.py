from unittest import TestCase
from single_number import Solution

class TestSolution(TestCase):
    def test_single_number(self):
        self.assertTrue(Solution.singleNumber(self,[2,2,1]))
        self.assertTrue(Solution.singleNumber(self,[4,1,2,1,2]))
        self.assertTrue(Solution.singleNumber(self,[1]))
