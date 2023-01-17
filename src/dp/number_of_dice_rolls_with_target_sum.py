"""
1
6
3
"""
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # num of the ways by using 0 .. i -1 dices and sum is j
        # dp[n][target]
        # dp[i][j] = 0
        # dp[0][0] = 1
        # dp[i][j+a] += dp[i][j] + a (1 <= a <= k)
        dp = [[0] * (target + 1) for _ in range(n+1)]
        dp[0][0] = 1
        mod = 1000000000 + 7
        for i in range(n):
            for j in range(target):
                for face in range(1, k+1):
                    if j + face <= target:
                        dp[i+1][j+face] += dp[i][j]
                        dp[i+1][j+face] %= mod
        return dp[n][target]
