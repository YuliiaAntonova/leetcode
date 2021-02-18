from unittest import TestCase
from kids_the_greatest_number import Solution

class TestSolution(TestCase):
    def test_kids_with_candies(self):
        self.assertTrue(Solution.kidsWithCandies(self,[2,3,5,1,3],3))
        self.assertTrue(Solution.kidsWithCandies(self, [4,2,1,1,2],1))
        self.assertTrue(Solution.kidsWithCandies(self, [12,1,12],10))
