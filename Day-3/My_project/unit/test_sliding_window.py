import pytest
from dsa.sliding_window import longest_substring

class TestSlidingWindow:
    def test_standard_case(self):
        """Happy path: abcabcbb → 3"""
        assert longest_substring("abcabcbb") == 3
    
    def test_all_same(self):
        """Edge: bbbbb → 1"""
        assert longest_substring("bbbbb") == 1
    
    def test_empty(self):
        """Edge: "" → 0"""
        assert longest_substring("") == 0
    
    def test_single_char(self):
        """Edge: "a" → 1"""
        assert longest_substring("a") == 1
    
    def test_three_unique(self):
        """Edge: "abc" → 3"""
        assert longest_substring("abc") == 3
    
    def test_case_sensitive(self):
        """Production: "aA" → 2 (case sensitive)"""
        assert longest_substring("aA") == 2
