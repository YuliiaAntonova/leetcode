from unittest import TestCase
from goal_parser import Solution

class TestSolution(TestCase):
    def test_interpret(self):
        self.assertTrue(Solution.interpret(self,"G()()()()(al)"))
        self.assertTrue(Solution.interpret(self,"(al)G(al)()()G"))

