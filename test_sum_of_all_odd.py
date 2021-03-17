from unittest import TestCase
from sum_of_all_odd import Solution

class TestSolution(TestCase):
    def test_sum_odd_length_subarrays(self):
        self.assertTrue(Solution.sumOddLengthSubarrays(self,[1,4,2,5,3]))
