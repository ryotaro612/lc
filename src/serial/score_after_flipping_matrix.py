class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        res = n_rows * (1<<(n_cols-1))
        
        for c in range(1, n_cols):
            counter = 0
            for r in range(n_rows):
                if grid[r][c] == grid[r][0]:
                    counter += 1
            
            res += max(counter, n_rows - counter) * (1<<(n_cols - c-1))
        return res 
