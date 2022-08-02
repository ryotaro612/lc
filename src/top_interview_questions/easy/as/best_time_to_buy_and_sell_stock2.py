"""
1 5 10 -> 9
buy 1, sell 5(1), buy 5, sell 10(5)
buy 1 sell 10(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        result = 0
        for i in range(n-1):
            result += max(0, prices[i+1] - prices[i])
        return result
