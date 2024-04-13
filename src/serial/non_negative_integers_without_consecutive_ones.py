class Solution:
    def findIntegers(self, n: int) -> int:
        n_str = bin(n)[2:]
        m = len(n_str)
        dp = [[[0] * 2 for _ in range(2)] for _ in range(m)]
        dp[0][0][1] = 1
        dp[0][1][0] = 1
        # print(n_str, m)
        for i in range(1, m):
            if n_str[i] == '0':
                dp[i][0][0] = dp[i-1][0][0] + dp[i-1][0][1]
            else:
                dp[i][0][1] = dp[i-1][0][0]

                dp[i][1][0] = dp[i-1][0][0] + dp[i-1][0][1]                
                
            dp[i][1][0] += dp[i-1][1][0] + dp[i-1][1][1]
            dp[i][1][1] += dp[i-1][1][0]

            # print(dp[i][0], dp[i][1])
            
        return sum(dp[m-1][0]) + sum(dp[m-1][1])
