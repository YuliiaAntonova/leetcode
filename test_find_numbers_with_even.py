from unittest import TestCase
from find_numbers_with_even import Solution

class TestSolution(TestCase):
    def test_find_numbers(self):
        self.assertTrue(Solution.findNumbers(self,[12,345,2,6,7896]))
        self.assertTrue(Solution.findNumbers(self,[555,901,482,1771]))
