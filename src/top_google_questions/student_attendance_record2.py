class Solution:
    def checkRecord(self, n: int) -> int:
        """
        dp[3][2]
        dp[i][j]: i num of consecutive L days 0, 1, 2, j num of total 'A'
        
        dp[0][0] = dp[0][0]
        dp[1][0] = dp[0][0] + dp[1][0]
        dp[0][1] = dp[0][0] + dp[0][1]
        """
        dp = [[0] * 2 for _ in range(3)]
        dp[0][0] = 1
        
        mod = (10**9+7)
        for _ in range(n):
            next_dp = [[0] * 2 for _ in range(3)]
            
            next_dp[0][0] = dp[0][0]
            next_dp[0][0] += dp[1][0]
            next_dp[0][0] %= mod
            next_dp[0][0] += dp[2][0]
            next_dp[0][0] %= mod
            
            
            next_dp[1][0] = dp[0][0]
            next_dp[2][0] = dp[1][0]
            
            next_dp[0][1] = dp[0][0]
            for item in [dp[1][0], dp[2][0], dp[0][1], dp[1][1], dp[2][1]]:
                next_dp[0][1] += item
                next_dp[0][1] %= mod
            
            next_dp[1][1] = dp[0][1]
            next_dp[2][1] = dp[1][1]
            dp = next_dp
        result = 0
        for i in range(3):
            for j in range(2):
                result += dp[i][j]
                result %= mod
        return result % mod
    
