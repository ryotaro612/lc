class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i, p in enumerate(prob):
            for j in range(i + 1):
                dp[i + 1][j] += dp[i][j] * (1 - p)
                dp[i + 1][j + 1] += dp[i][j] * p

        return dp[n][target]
