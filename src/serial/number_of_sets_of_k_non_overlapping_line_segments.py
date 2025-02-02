class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # dp[i][j] # # of ways to j [0, i] dp[n][k] i-1

        # i dp[0..i-1][0..k]
        # dp[i][0] = 1
        # dp[i][j] = dp[0][j-1] + dp[1][j-1] + ...dp[i-1][j-1] + dp[i-1][j]
        dp = [[0] * (k+1) for _ in range(n+1)]
        dp[0][0] = 1
        mod = 10**9 + 7

        dp_sum = [0] * (k+1)
        dp_sum[0] = 1
        for i in range(1, n):
            dp[i][0] = 1
            for j in range(1, k+1):
                """
                temp = 0
                for l in range(i):
                    temp += dp[l][j-1]
                    temp %= mod

                dp[i][j] = (temp + dp[i-1][j]) % mod
                """
                dp[i][j] = (dp_sum[j-1] + dp[i-1][j]) % mod
                dp_sum[j-1] += dp[i][j-1]
                dp_sum[j-1] %= mod
        return dp[n-1][k]
