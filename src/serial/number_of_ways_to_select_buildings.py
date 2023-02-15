class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        010 or 101
        123    456  
        dp[i][0] -> # of patterns of selecting none of buildings 
        dp[i][1] ->               of selecting the first 0 in 010 from [0..i]
        dp[i][2] ->                                      1 in 010
        dp[n][3] + dp[n][6]
        """

        n = len(s)
        dp, next_dp = [0] * 7, [0] * 7
        dp[0] = 1
        for i, num in enumerate(s):
            for j in range(7):
                next_dp[j] = dp[j]

            if num == '1':
                next_dp[2] += dp[1]
                next_dp[4] += dp[0]
                next_dp[6] += dp[5]
            else:
                next_dp[1] += dp[0]
                next_dp[3] += dp[2]
                next_dp[5] += dp[4]

            dp, next_dp = next_dp, dp
        return dp[3] + dp[6]
           
