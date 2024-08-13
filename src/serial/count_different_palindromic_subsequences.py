class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        mod = 10**9+7
        for distance in range(1, n):
            for i in range(n - distance):
                j = i + distance
                if s[i] != s[j]:
                    dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]
                else:
                    low = i + 1
                    high = j - 1
                    while low <= high and s[low] != s[j]:
                        low += 1
                    while low <= high and s[high] != s[j]:
                        high -= 1

                    if low > high:
                        dp[i][j] = dp[i+1][j-1] * 2 + 2
                    elif low == high:
                        dp[i][j] = dp[i+1][j-1] * 2 + 1
                    else:
                        dp[i][j] = dp[i+1][j-1] * 2 - dp[low+1][high-1]
                    
                dp[i][j] %= mod
        return dp[0][n-1]
