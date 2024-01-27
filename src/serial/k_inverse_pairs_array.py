class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        prefix = [1] * (k+2)
        prefix[0] = 0
        dp = [0] * (k+1)
        dp[0] = 1
        for i in range(n-2, -1, -1):
            for j in range(k+1):
                dp[j] = prefix[j+1] - prefix[max(0, j-(n-i-1))]
                dp[j] %= mod
            for j in range(k+1):
                prefix[j+1] = (dp[j] + prefix[j]) % mod
        return dp[k]
        
        
        """
        dp = [[0] * (k+1) for _ in range(n)]
        mod = 10**9+7
        dp[n-1][0] = 1
        for i in range(n-2, -1, -1):
            for j in range(k+1):
                for a in range(n-i):
                    if j - a >= 0:
                        dp[i][j] += dp[i+1][j-a]
                        dp[i][j] %= mod
                    else:
                        break
        return dp[0][k]
        """
