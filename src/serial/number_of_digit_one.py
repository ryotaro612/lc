"""
10
0
"""
class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        n_digits = len(s)
        dp = [[0] * 2 for _ in range(n_digits+1)]
        
        for i, d in enumerate([ord(c) - ord('0') for c in s]):
            if d == 0:
                dp[i+1][0] += dp[i][0]
            elif d == 1:
                dp[i+1][0] += dp[i][0] + 1
                dp[i+1][1] += dp[i][0]
            else:
                dp[i+1][0] += dp[i][0]
                dp[i+1][1] += dp[i][0] * d + 1
        
            dp[i+1][1] += dp[i][1] * 10
            if i > 0:
                dp[i+1][1] += int(s[:i])

        # print(dp)
        return sum(dp[n_digits])
