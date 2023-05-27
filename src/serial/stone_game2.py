"""
[1]
1
"""
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * (n+1) for _ in range(n+1)]
        prefix_sum = [0] * (n+1)
        for i, pile in enumerate(piles):
            prefix_sum[i+1] = prefix_sum[i] + pile

        for i in range(n-1, -1, -1):
            for m in range(n, -1, -1):

                for step in range(1, 2*m+1):
                    if i + step <= n:
                        dp[i][m] = max(dp[i][m], prefix_sum[i+step] - prefix_sum[i] + prefix_sum[n] - prefix_sum[i+step] - dp[i+step][min(n, max(m, step))])
                    else:
                        dp[i][m] = max(dp[i][m], prefix_sum[n] - prefix_sum[i])
        # print(dp)
        return dp[0][1]
                
