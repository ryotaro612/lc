from collections import defaultdict

class Solution:
    def maxA(self, n: int) -> int:
        # dp[i][j] max A by pressing i and hold j 'A' in buffer
        # 0<=i<=n
        dp = [defaultdict(lambda: -float('inf')) for _ in range(n+3)]
        dp[0][0] = 0
        for i in range(n):
            for j in dp[i]:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + 1)
                dp[i+2][dp[i][j]] = max(dp[i+2][dp[i][j]], dp[i][j])
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + j)
        return max(dp[n].values())
        
