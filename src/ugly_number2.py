
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        a, b, c = 0, 0, 0
        for i in range(n-1):
            dp.append(min(dp[a] * 2, dp[b] * 3, dp[c] * 5))
            if dp[-1] == dp[a] * 2:
                a += 1
            if dp[-1] == dp[b] * 3:
                b += 1
            if dp[-1] == dp[c] * 5:
                c += 1
        return dp[-1]
