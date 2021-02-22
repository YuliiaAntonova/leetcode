from unittest import TestCase
from subtract_the_product_and_sum import Solution

class TestSolution(TestCase):
    def test_subtract_product_and_sum(self):
        self.assertTrue(Solution.subtractProductAndSum(self,234))
        self.assertTrue(Solution.subtractProductAndSum(self, 4421))

