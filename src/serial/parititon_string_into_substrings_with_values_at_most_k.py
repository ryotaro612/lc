import math
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        """
        n = len(s)
        dp[0..n-1]  = inf
        dp[i] = s[]
        dp[n-1]
        dp[i]
                    dp[i-j] int(s[i-j:i+1])
        dp[i] = 1 + min(dp[i-1], dp[i-2], dp[i-3],..)
        dp[n]
        """
        n = len(s)
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        for i in range(1, n+1):
            j = i - 1
            while j >= 0 and int(s[j:i]) <= k:
                dp[i] = min(dp[i], 1 + dp[j])
                j -= 1
        if dp[n] == math.inf:
            return -1
        return dp[n]
