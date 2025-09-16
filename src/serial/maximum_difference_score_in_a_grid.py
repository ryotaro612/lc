class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        """
        dp[r][c]
        dp[n_rows-1][n_cols-1] = grid[-1][-1]
        n_rows-2..0
        maxi=grid[-1][-1]
        dp[-1][n_cols-i] i=2,3... = maxi - grid[-1][n_cols-i]
        col_maxi[n_cols-i] = max(col_maxi[n_cols-i], dp[-1])
        maxi = max(maxi, maxi-grid...)
        col
        """
        n_rows = len(grid)
        n_cols = len(grid[0])
        dp = [[0] * n_cols for _ in range(n_rows)]
        col_maxi = [0] * n_cols
        maxi = 0

        for r in range(n_rows-1, -1, -1):
            maxi = 0
            for c in range(n_cols-1, -1, -1):
                dp[r][c] = max(maxi - grid[r][c], col_maxi[c] - grid[r][c])
                maxi = max(maxi, grid[r][c], dp[r][c] + grid[r][c])
                col_maxi[c] = max(col_maxi[c], grid[r][c], dp[r][c] + grid[r][c])
                
        # 1 2 3 4
        result = -float('inf')
        for r in range(n_rows):
            for c in range(n_cols):
                if (r, c) != (n_rows-1, n_cols-1):
                    result = max(result, dp[r][c])
        
        return result
