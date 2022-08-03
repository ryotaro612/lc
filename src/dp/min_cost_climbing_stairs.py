"""
dp[0] = 0
dp[1] = 0
dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        
        dp = [0, 0]
        
        for i in range(2, n+1):
            current = min(dp[1] + cost[i-1], dp[0] + cost[i-2])
            dp[0] = dp[1]
            dp[1] = current
        return dp[1]
