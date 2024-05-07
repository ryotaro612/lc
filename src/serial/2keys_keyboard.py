class Solution:
    def minSteps(self, n: int) -> int:
        """
        dp[1][0] = 0
        dp[i][j]
        dp[i][j+i] += 1
        dp[i+j][j] += 1
        """
        dp = [[float('inf')] * (n+1) for _ in range(n+1)]
        dp[1][0] = 0
        for i in range(1, n+1):
            for j in range(n+1):
                dp[i][i] = min(dp[i][i], dp[i][j] + 1)
                if i + j <= n:
                    dp[i+j][j] = min(dp[i+j][j], dp[i][j] + 1)
    
        return min(dp[n])
