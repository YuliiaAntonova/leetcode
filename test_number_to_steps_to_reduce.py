from unittest import TestCase
from number_to_steps_to_reduce import Solution

class TestSolution(TestCase):
    def test_number_of_steps(self):
        self.assertTrue(Solution.numberOfSteps(self,123))
