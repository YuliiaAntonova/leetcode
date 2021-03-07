from unittest import TestCase
from count_items_matching import Solution

class TestSolution(TestCase):
    def test_count_matches(self):
        self.assertTrue(Solution.countMatches(self,[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],"color","silver"))
        self.assertTrue(Solution.countMatches(self,[["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],"type","phone"))

