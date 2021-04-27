from unittest import TestCase
from height_checker import Solution

class TestSolution(TestCase):
    def test_height_checker(self):
        self.assertTrue(Solution.heightChecker(self,[1,1,4,2,1,3]))
        self.assertTrue(Solution.heightChecker(self,[5,1,2,3,4]))
        self.assertLogs(Solution.heightChecker(self,[1,2,3,4,5]))
