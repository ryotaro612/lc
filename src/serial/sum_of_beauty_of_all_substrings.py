class Solution:
    def beautySum(self, s: str) -> int:
        """
        dp[i][26] dp[i][j] freq s[:i]
        s[i:j]
        dp[j][*] - dp[i][*]
        """
        n = len(s)
        dp = [[0] * 26 for _ in range(n+1)]

        for i in range(n):
            for c in range(26):
                dp[i+1][c] = dp[i][c]
            dp[i+1][ord(s[i]) - ord('a')] += 1
        
        result = 0
        for i in range(n):
            for j in range(i+1, n+1):
                maxi = 0
                mini = n + 1
                for c in range(26):
                    maxi = max(maxi, dp[j][c] - dp[i][c])
                    if dp[j][c] > dp[i][c]:
                        mini = min(mini, dp[j][c] - dp[i][c])
                result += maxi-mini
        
        return result
