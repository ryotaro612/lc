class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        memo = [[-float('inf')] * n_cols for _ in range(n_rows)]
        for r in range(n_rows):
            memo[r][0] = 0

        for c in range(n_cols-1):
            for r in range(n_rows):
                if r and grid[r][c] < grid[r-1][c+1]:
                    memo[r-1][c+1] = max(memo[r-1][c+1], memo[r][c] + 1)
                if grid[r][c] < grid[r][c+1]:
                    memo[r][c+1] = max(memo[r][c+1], memo[r][c] + 1)
                if r < n_rows - 1 and grid[r][c] < grid[r+1][c+1]:
                    memo[r+1][c+1] = max(memo[r+1][c+1], memo[r][c] + 1)
        result = -float('inf')
        for r in range(n_rows):
            for c  in range(n_cols):
                result = max(result, memo[r][c])
        return max(result, 0)
