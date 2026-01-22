import pytest
from dsa.kadanes_stock import test_max_profit 
class kadanes:
    def test_rising_prices(self):
        """Classic profitable case"""
        assert test_max_profit([7,1,5,3,6,4]) == 5
    
    def test_falling_prices(self):
        """No profit possible"""
        assert test_max_profit([7,6,4,3,1]) == 0
    
    def test_single_day(self):
        """Edge case"""
        assert test_max_profit([7]) == 0
    
    def test_two_days_profit(self):
        """Minimal profitable"""
        assert test_max_profit([1,2]) == 1
    
    def test_two_days_loss(self):
        """Minimal loss"""
        assert test_max_profit([2,1]) == 0
    
    def test_empty(self):
        """Defensive"""
        assert test_max_profit([]) == 0