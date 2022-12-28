class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        """
        dp[i][j][k] the max profit I i in [0..n], j in [0,2]
        k = 1 if I hold a stock, k =0 if I don't hold s stock
        """
        n = len(prices)
        dp = [[[-float('inf')] * 2 for _ in range(3)] for _ in range(n+1)]
        dp[0][0][0] = 0 
        for i in range(n):
            price = prices[i]
            for j in range(3):
                dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][0])
                dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][1])
                if j < 2:
                    # buy a stock
                    dp[i+1][j+1][1] = max(dp[i+1][j+1][1], dp[i][j][0] - price)
                if 0 < j:
                    # sell a stock
                    dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][1] + price)
        result = -float('inf')
        for i in range(3):
            result = max(result, dp[n][i][0])
        return result
