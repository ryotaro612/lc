"""
dp[i][j]

# of patters to paint 0 - ith fences and the ith fence is jth color.

dp[i][j] = sum(dp[i-1]) - dp[i-2][j]

sum(sum[i])

1
1

3
2

4
2
"""
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        dp = [0] * n
        dp[0] = 1
        dp[1] = k
        for i in range(2, n):
            dp[i] = dp[i-1] * (k-1) + dp[i-2] * (k-1)
        return dp[n-1] * k
