class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp, prefix = [0] * (n + 1), [0] * (n + 1)

        prefix[0] = 0
        dp[0] = 1
        for i in range(n + 1):
            if i:
                prefix[i] += prefix[i - 1]
                dp[i] = prefix[i]
            if i < k:
                prob = dp[i] / maxPts
                prefix[i + 1] += prob
                if i + maxPts + 1 <= n:
                    prefix[i + maxPts + 1] -= prob

        return sum(dp[k:])
