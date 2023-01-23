class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])

        perimeter = 0

        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == 0:
                    continue
                for next_r, next_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
                    if 0 <= next_r < n_row and 0 <= next_c < n_col:
                        if grid[next_r][next_c] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1
        return perimeter
