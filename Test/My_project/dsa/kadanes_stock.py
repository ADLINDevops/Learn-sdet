def test_max_profit(prices):
    """Kandane's Algrithm for max profilt from stocks"""
    if len(prices)<2:
        return 0
    #todays rate,is price
    #sell price
    #profit
    max_profit=0
    min_profit=prices[0]
    for price in prices[1:]:# consider from index 1
        min_profit=min(price,min_profit)# minimum price
        
        daily_profit=price-min_profit# if sold today
        max_profit=max(daily_profit,max_profit)#maximum profit
    return max_profit   

print(test_max_profit([7,1,5,3,6,4]))