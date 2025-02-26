class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * 2 for i in range(n)]
        if arr[0] % 2:
            dp[0][1] = 1
        else:
            dp[0][0] = 1
        
        mod = 10**9 + 7
        for i in range(1, n):
            if arr[i] % 2:
                dp[i][1] += 1
                dp[i][1] += dp[i-1][0]
                dp[i][0] += dp[i-1][1]
            else:
                dp[i][0] += 1
                dp[i][0] += dp[i-1][0]
                dp[i][1] += dp[i-1][1]
            dp[i][0] %= mod
            dp[i][1] %= mod

        result = 0
        for i in range(n):
            result += dp[i][1]
            result %= mod
        return result
