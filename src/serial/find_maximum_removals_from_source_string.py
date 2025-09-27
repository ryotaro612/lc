class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        """
        dp[i][j] source[i:] pattern[j:]
        dp[0][0]
        dp[i][j] s[i] == p[j] i in t => dp[i][j] = 1 + dp[i+1][j]
        dp[i]    s[i] == p[j] i not in t =>dp[i+1][j+1]
        s[i] != p[j] i in t => 1 + dp[i+1][j]
        s[i] != s[j] i not in t => dp[i+1][j]
        """
        n_s = len(source)
        n_p = len(pattern)
        targets = set(targetIndices)
        dp = [[0] * (n_p + 1) for _ in range(n_s+1)]
        for i in range(n_s, -1, -1):
            for j in range(n_p, -1, -1):
                if i == n_s:
                    if j < n_p:
                        dp[i][j] = -float('inf')                    
                    continue
                # print(i, j)
                if j == n_p:
                    if i in targets:
                        # print(i, j)
                        dp[i][j] = 1 + dp[i+1][j]
                    else:
                        dp[i][j] = dp[i+1][j]
                    continue

                if source[i] == pattern[j]:
                    if i in targets:
                        dp[i][j] = max(1 + dp[i+1][j], dp[i+1][j+1])
                    else:
                        dp[i][j] = dp[i+1][j+1]
                else:
                    if i in targets:
                        dp[i][j] = 1 + dp[i+1][j]
                    else:
                        dp[i][j] = dp[i+1][j]
        # print(dp)
        return dp[0][0]
