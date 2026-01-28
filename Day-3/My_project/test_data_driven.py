import pytest
from dsa.sliding_window import longest_substring

class TestParameter():
    @pytest.mark.parametrize("input_str,expected",[
        ("abcabcba",3),
        ("bbbb",1),
        ("",0),
        ("aA",2),
        ("pwwwkew",3),
        ("abc",3),
        ("abba",2),])

    def test_parameter(self,input_str,expected):
        """ Test case with Data Driven testing"""
        assert longest_substring(input_str)==expected