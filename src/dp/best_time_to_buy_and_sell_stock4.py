"""
dp[i] = (v, [()])
0 <= i <= 1001
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[-float('inf')] * 2 for _ in range(k+1)] for _ in range(n+1)]
        dp[0][0][0] = 0
        
        for i, price in enumerate(prices):
            for j in range(k+1):
                dp[i+1][j][0] = max(dp[i][j][0], dp[i+1][j][0])
                dp[i+1][j][1] = max(dp[i][j][1], dp[i+1][j][1])
                dp[i+1][j][0] = max(dp[i][j][1] + price, dp[i+1][j][0])
                if j < k:
                    dp[i+1][j+1][1] = max(dp[i][j][0] - price, dp[i+1][j+1][1])
                    dp[i+1][j+1][1] = max(dp[i+1][j][0] - price, dp[i+1][j+1][1])
            # print(dp[i+1])
        result = -float('inf')
        for i in range(k+1):
            for j in [0, 1]:
                result = max(result, dp[n][i][j])
                
        return result
