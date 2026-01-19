import pytest
from Two_sum import two_sum

#class used here for organised structure and as container
class TestTwoSum:
    def standard_test_case(self):
        """Standard"""
        result=two_sum([2,7,11,15],9)
        assert result==[0,1]
     

