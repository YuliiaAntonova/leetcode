from unittest import TestCase
from richest_customer import Solution

class TestSolution(TestCase):
    def test_maximum_wealth(self):
        self.assertTrue(Solution.maximumWealth(self,[[1,2,3],[3,2,1]]))
        self.assertTrue(Solution.maximumWealth(self,[[1,5], [7,3], [3,5]]))
        self.assertTrue(Solution.maximumWealth(self, [[2,8,7], [7,1,3], [1,9,5]]))


