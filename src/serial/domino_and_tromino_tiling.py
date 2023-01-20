class Solution:
    def numTilings(self, n: int) -> int:
        """
        ""
        dp[i][j]
        dp[2][2]
        ...
        ...
        dp[3][3] += dp[2][2]
        
        dp[2][1]
        ..
        .
        d[0]
        0<=i, j<=n
        
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        dp[0][0] = 1
        mod = 1000000000 + 7
        for i in range(n):
            dp[i+1][i+1] += dp[i][i]
            dp[i+1][i+1] %= mod
            if i:
                dp[i+1][i] += dp[i-1][i]
                dp[i+1][i] %= mod
                dp[i][i+1] += dp[i][i-1]
                dp[i][i+1] %= mod
                
                dp[i+1][i+1] += dp[i-1][i-1]
                dp[i+1][i+1] %= mod
                
                dp[i+1][i] += dp[i-1][i-1]
                dp[i+1][i] %= mod
                dp[i+1][i+1] += dp[i-1][i]
                dp[i+1][i+1] %= mod
                dp[i+1][i+1] += dp[i][i-1]
                dp[i+1][i+1] %= mod
                dp[i][i+1] += dp[i-1][i-1]
                dp[i][i+1] %= mod
                
            #print(i, dp)
        return dp[n][n]
