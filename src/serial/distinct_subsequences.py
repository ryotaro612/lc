class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n_s = len(s)
        n_t = len(t)

        dp = [[0] * (n_t + 1) for _ in range(n_s + 1)]
        for i in range(n_s + 1):
            dp[i][0] = 1

        for i in range(n_s):
            for j in range(n_t):
                if s[i] == t[j]:
                    dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] += dp[i][j+1]
        return dp[n_s][n_t]
