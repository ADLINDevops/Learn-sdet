import pytest
from dsa.interview_day import longest_test_sequence

class testalues:
    def test_duplicatevalue(self):
        assert longest_test_sequence(["test_login","test_PII","test_cart","test_cart","test_out","test_PII"])==4
    def test_onevalue(self):
        assert longest_test_sequence(["test_login"])==1
    def test_empty(self):
        assert longest_test_sequence([])==0
    def test_number(self):
        assert longest_test_sequence([1,1,2,3])==3
    def test_allduplicates(self):
        assert longest_test_sequence(["test_login","test_login"])==1
    
    