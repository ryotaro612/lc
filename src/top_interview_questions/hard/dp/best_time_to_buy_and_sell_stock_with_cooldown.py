"""
dp[0<=i<5000][0<=j<1001] = max profit
dp[i][0]                 = max(dp[i-1][0], dp[i-1][1..j..1001] + price[i])

dp[i][1..j..1001]        = dp[i-1][j]
dp[i][price[i]]          = dp[i-2][0] - price[i]

max(dp[len(prices)-1][0..1001])
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        dp = [[-float('inf')] * 1001 for _ in range(2)]
        # dp[1] yesterday
        # dp[0] 2days ago
        no_stock = [0, 0]
        # dp[i][0] have stock that I bought by $0
        
        for price in prices:
            today = list(dp[1])
            today_no_stock = no_stock[1]
            # sell
            for stock in range(0, 1001):
                today_no_stock = max(today_no_stock, dp[1][stock] + price)
            # buy
            today[price] = max(today[price], no_stock[0] - price)
            
            dp[0], dp[1] = dp[1], today
            no_stock = [no_stock[1], today_no_stock]
            # print(no_stock[-1], ' -- ', dp[1])
        return max(no_stock[1], max(dp[1]))
