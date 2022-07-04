"""
"intention"
"execution"

""
""

"b"
"aaaab"

"a"
"ab"
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        # dp[i][j] is the result of minDistance(word1[:i], word2[:j])
        # dp[n][m]
        # O(n * m)
        dp = [[float('inf')] * (m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(m+1):
                if j == 0:
                    dp[i][j] = min(i, dp[i][j])
                elif i == 0:
                    dp[i][j] = min(j, dp[i][j])
                else:
                    # update dp[i][j]
                    # dp[i-1][j], dp[i-1][j-1]
                    # print(i, j, dp[i][j], dp[i-1][j])
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j])
                    dp[i][j] = min(dp[i][j-1]+ 1 , dp[i][j])
                    if word1[i-1] == word2[j-1]:
                        dp[i][j] = min(dp[i-1][j-1], dp[i][j])
                    else:
                        dp[i][j] = min(dp[i-1][j-1]+1, dp[i][j])
                #print(word1[:i], word2[:j], dp[i][j])
        
        return dp[n][m]
