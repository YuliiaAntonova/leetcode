from unittest import TestCase
from split_string_in_balanced import Solution

class TestSolution(TestCase):
    def test_balanced_string_split(self):
        self.assertTrue(Solution.balancedStringSplit(self,'RLLLLRRRLR'))
