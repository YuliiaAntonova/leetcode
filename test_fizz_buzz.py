from unittest import TestCase
from fizz_buzz import Solution

class TestSolution(TestCase):
    def test_fizz_buzz(self):
        self.assertTrue(Solution.fizzBuzz(self,15))
