from unittest import TestCase
from merge_strings_alternatery import Solution

class TestSolution(TestCase):
    def test_merge_alternately(self):
        self.assertTrue(Solution.mergeAlternately(self,"abc","pqr"))
        self.assertTrue(Solution.mergeAlternately(self,"ab","pqrs"))
