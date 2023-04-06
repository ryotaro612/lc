class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        for r, c in [(r,c) for c in range(n_col) for r in [0, n_row-1]] + [(r, c) for r in range(n_row) for c in [0, n_col -1]]:
            self.makeWater(r, c, grid)

        result = 0
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] == 0:
                    result += 1
                    self.makeWater(r, c, grid)
        return result

    def makeWater(self, r, c, grid):
        n_row = len(grid)
        n_col = len(grid[0])

        if 0 <= r < n_row and 0 <= c < n_col and grid[r][c] == 0:
            grid[r][c] = 1
            for n_r, n_c in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                self.makeWater(n_r, n_c, grid)
