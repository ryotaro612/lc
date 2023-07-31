class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1, n2 = len(s1), len(s2)
        dp = [[float('inf')] * (n2+1) for _ in range(n1+1)]

        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0:
                    if j == 0:
                        dp[0][0] = 0
                    else:
                        dp[0][j] = dp[0][j-1] + ord(s2[j-1])
                else:
                    if j == 0:
                        dp[i][0] = dp[i-1][0] + ord(s1[i-1])
                    else: # i and j
                        dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
                        if s1[i-1] == s2[j-1]:
                            dp[i][j] = min(dp[i][j], dp[i-1][j-1])
                        else:
                            dp[i][j] = min(dp[i][j], dp[i-1][j-1] + ord(s1[i-1]) + ord(s2[j-1]))
        
        return dp[n1][n2]
                        
