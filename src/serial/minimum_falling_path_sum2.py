class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        n = len(grid[0])
        dp = list(grid[0])

        for r in range(1, n):
            next_dp = [float('inf')] * n
            for c in range(n):
                for c2 in range(n):
                    if c2 != c:
                        next_dp[c2] = min(next_dp[c2], dp[c] + grid[r][c2])
            dp = next_dp
        
        return min(dp)
