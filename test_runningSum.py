from unittest import TestCase
from runningSum import Solution

class TestSolution(TestCase):
    def test_running_sum(self):
        self.assertTrue(Solution.runningSum(self,[1, 2, 3, 4]))
