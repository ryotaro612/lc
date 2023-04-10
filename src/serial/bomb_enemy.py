class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])

        enemies = [[0] * n_col for _ in range(n_row)]

        for dc, c in [[1, 0], [-1, n_col - 1]]:
            for r in range(n_row):
                self.find(r, c, 0, dc, grid, enemies)
        for dr, r in [[1, 0], [-1, n_row - 1]]:
            for c in range(n_col):
                self.find(r, c, dr, 0, grid, enemies)
        # print(enemies)
        return max([enemies[r][c] for r in range(n_row) for c in range(n_col)])
    def find(self, r, c, dr, dc, grid, enemies):
        count = 0
        n_row = len(grid)
        n_col = len(grid[0])
        while 0 <= r < n_row and 0 <= c < n_col:
            if grid[r][c] == '0':
                enemies[r][c] += count
            elif grid[r][c] == 'W':
                count = 0
            else: # E
                count += 1
            r += dr
            c += dc
        
