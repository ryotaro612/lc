class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = max(prices)
        dp = [-float('inf')] * 2
        dp[0] = 0
        
        for price in prices:
            next_dp = [None, None]
            next_dp[0] = max(dp[0], dp[1] + price)
            next_dp[1] = max(dp[1], dp[0] -fee - price)
            dp = next_dp
            
        return max(dp)
    
            
