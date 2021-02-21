from unittest import TestCase
from how_many_numbers_are_smaller import Solution

class TestSolution(TestCase):
    def test_smaller_numbers_than_current(self):
        self.assertTrue(Solution.smallerNumbersThanCurrent(self, [8,1,2,2,3]))
        self.assertTrue(Solution.smallerNumbersThanCurrent(self, [6,5,4,8]))
        self.assertTrue(Solution.smallerNumbersThanCurrent(self, [7,7,7,7]))