"""
dp[i][3] = anwer of [n = i][0 = red][1 = blue][2 = green]
dp[i+1][0] = min(dp[i][1], dp[i][2]) + costs[i+1][0]
"""
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0] * 3
        for cost in costs:
            next_dp = [0] * 3
            next_dp[0] = min(dp[1], dp[2]) + cost[0]
            next_dp[1] = min(dp[0], dp[2]) + cost[1]
            next_dp[2] = min(dp[0], dp[1]) + cost[2]
            dp = next_dp
        return min(d)
