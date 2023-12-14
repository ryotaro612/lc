class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # m x n
        n_rows, n_cols = len(grid), len(grid[0])
        ones_row = [0] * n_rows
        ones_col = [0] * n_cols
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c]:
                    ones_row[r] += 1
                    ones_col[c] += 1
        diff = [[0] * n_cols  for _ in range(n_rows)]

        for r in range(n_rows):
            for c in range(n_cols):
                diff[r][c] = ones_row[r] + ones_col[c] - (n_cols - ones_row[r]) - (n_rows - ones_col[c])
        
        return diff
