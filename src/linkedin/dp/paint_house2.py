"""
[[10,15,12,14,18,5],[5,12,18,13,15,8],[4,7,4,2,10,18],[20,9,9,19,20,5],[10,15,10,15,16,20],[9,6,11,10,12,11],[7,10,6,12,20,8],[3,4,4,18,10,2]]
"""
class Solution:
    """
    dp[i][j] = the min cost to paint 0 .. i houses and i-1th house is paited with jth color.
    dp[i-1][*]
    result = min(dp[n][*])
    """
    def minCostII(self, costs: List[List[int]]) -> int:
        n_colors = len(costs[0])
        dp = [cost for cost in costs[0]]
        for house_cost in costs[1:]:
            mini_left, mini_right = [float('inf')] * n_colors, [float('inf')] * n_colors
            # min_left[i] is min cost between 0 .. i-1
            # min(min_left[i], min_right[i])
            for i in range(1, n_colors):
                mini_left[i] = min(mini_left[i-1], dp[i-1])
            for i in range(n_colors-2, -1, -1):
                mini_right[i] = min(mini_right[i+1], dp[i+1])
            # print(mini_left, mini_right)
            next_dp = [0] * n_colors
            for i in range(n_colors):
                next_dp[i] = house_cost[i] + min(mini_left[i], mini_right[i])
            dp = next_dp
        
        return min(dp)
