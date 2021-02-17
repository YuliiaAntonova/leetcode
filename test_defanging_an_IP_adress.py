from unittest import TestCase
from defanging_an_IP_adress import Solution

class TestSolution(TestCase):
    def test_defang_ipaddr(self):
        self.assertTrue(Solution.defangIPaddr(self,"1.1.1.1"))
        self.assertTrue(Solution.defangIPaddr(self, "255.100.50.0"))
