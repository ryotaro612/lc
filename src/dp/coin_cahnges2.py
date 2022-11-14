"""
5
[1,2,5]

3
[2]

10
[10]
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(amount+1):
                dp[i+1][j] += dp[i][j]
                if j + coins[i] <= amount:
                    dp[i+1][j+coins[i]] += dp[i+1][j]
        
        return dp[n][amount]
