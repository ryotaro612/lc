"""
[0,2,1,2,0]
[[1,10],[10,1],[10,1],[1,10],[5,1]]
5
2
3

[3,1,2,3]
[[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
4
3
3
"""
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # dp[i][j] running the minimum cost  
        dp = [[float('inf')] * (m+1) for _ in range(n)]
        if houses[0] == 0:
            for i in range(n):
                dp[i][1] = cost[0][i]
        else:
            color = houses[0] - 1
            dp[color][1] = 0
        # print( dp)
        for h_i in range(1, m):
            next_dp = [[float('inf')] * (m+1) for _ in range(n)]
            if houses[h_i] == 0:
                for color in range(n):
                    for prev_color in range(n):
                        for n_neigh in range(1, h_i+1):
                            if color == prev_color:
                                next_dp[color][n_neigh] = min(
                                    next_dp[color][n_neigh], 
                                    dp[prev_color][n_neigh] + cost[h_i][color]
                                )
                            else:
                                next_dp[color][n_neigh+1] = min(
                                    next_dp[color][n_neigh+1], 
                                    dp[prev_color][n_neigh] + cost[h_i][color]
                                )
            else:
                color = houses[h_i] - 1
                for prev_color in range(n):
                    for n_neigh in range(1, h_i+1):
                        if color == prev_color:
                            next_dp[color][n_neigh] = min(
                                next_dp[color][n_neigh], dp[prev_color][n_neigh])
                        else:
                            next_dp[color][n_neigh+1] = min(
                                next_dp[color][n_neigh+1], dp[prev_color][n_neigh])
            dp = next_dp
            #print(dp)
        result = float('inf')
        for i in range(n):
            result = min(result, dp[i][target])
        return result if result < float('inf') else -1
