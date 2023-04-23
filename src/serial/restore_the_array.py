class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        mod = 10**9 + 7
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n):
            # print(i)
            if s[i] == '0':
                continue
            v = 0
            right = i
            while right < n and v * 10 + int(s[right]) <= k:
                # print('add', dp[i], right, v)
                dp[right+1] += dp[i]
                dp[right+1] %= mod
                v = v * 10 + int(s[right])
                right += 1
        
        return dp[n]
