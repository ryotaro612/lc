class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        dp = [[float('inf')] * n_col for _ in range(2)]
        dp[0][0] = 0
        for i in range(n_row):
            for j in range(n_col):
                dp[1][j] = grid[i][j]
                if j == 0:
                    dp[1][j] += dp[0][0]
                else:
                    dp[1][j] += min(dp[0][j], dp[1][j-1])
                dp[0] = list(dp[1])
        
        return dp[0][-1]
