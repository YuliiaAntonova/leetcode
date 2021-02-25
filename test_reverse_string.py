from unittest import TestCase
from reverse_string import Solution

class TestSolution(TestCase):
    def test_reverse_string(self):
        self.assertTrue(Solution.reverseString(self,["h","e","l","l","o"]))
        self.assertTrue(Solution.reverseString(self,["H","a","n","n","a","h"]))

