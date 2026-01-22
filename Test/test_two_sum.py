import pytest
from Two_sum import two_sum

#class used here for organised structure and as container
class TestTwoSum:
    def test_standard_case(self):
        """Classic interview example"""
        result = two_sum([2,7,11,15], 9)
        assert result == [0,1]
    
    def test_non_adjacent(self):
        """Real-world: numbers not next to each other"""
        result = two_sum([3,2,4], 6)
        assert result == [1,2]
    
    def test_duplicates(self):
        """QA thinking: What if same number twice?"""
        result = two_sum([3,3], 6)
        assert result == [0,1]
    
    def test_no_solution(self):
        """Production reality: Sometimes no answer"""
        result = two_sum([1], 10)
        assert result == []
    
    def test_empty_array(self):
        """Defensive programming"""
        result = two_sum([], 0)
        assert result == []
    
    def test_negatives(self):
        """Edge case mastery"""
        result = two_sum([-1,-2,-3], -3)
        assert result == [0,1]

