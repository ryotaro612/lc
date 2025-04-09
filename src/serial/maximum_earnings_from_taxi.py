class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        dp = [0] * (n+1)

        rides.sort(reverse=True)        
        
        for i in range(n+1):
            while rides and rides[-1][0] == i:
                _, end, tip = rides.pop()
                dp[end] = max(dp[end], dp[i] + end - i + tip)
            if i < n:
                dp[i+1] = max(dp[i+1], dp[i])
        return max(dp)
