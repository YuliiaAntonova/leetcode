from unittest import TestCase
from create_target_array import Solution

class TestSolution(TestCase):
    def test_create_target_array(self):
        self.assertTrue(Solution.createTargetArray(self,[0,1,2,3,4],[0,1,2,2,1]))
