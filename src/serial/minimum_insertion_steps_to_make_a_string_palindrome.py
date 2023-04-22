class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s) 
        dp = [[float('inf')] * (n+1) for _ in range(n+1)]
        for width in range(n+1):
            for left in range(n-width+1):
                right = left + width
                if right - left <= 1:
                    dp[left][right] = 0
                else:
                    # add
                    dp[left][right] = min(dp[left][right], 1 + dp[left+1][right])
                    dp[left][right] = min(dp[left][right], 1+ dp[left][right-1])
                    if s[left] == s[right - 1]:
                        dp[left][right] = min(dp[left][right], dp[left+1][right-1])
        return dp[0][n]
