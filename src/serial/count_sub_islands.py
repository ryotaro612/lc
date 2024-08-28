class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n_rows = len(grid2)
        n_cols = len(grid2[0])
        visit = [[False] * n_cols for _ in range(n_rows)]
        result = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if visit[r][c] or grid2[r][c]  == 0:
                    continue
                lands = set()
                self.find_lands(grid2, r, c, lands, visit)

                if all([grid1[n_r][n_c] for n_r, n_c in lands]):
                    result += 1
        
        return result
        
    
    def find_lands(self, grid, r, c, lands, visit):
        n_rows = len(grid)
        n_cols = len(grid[0])

        if not ((0 <= r < n_rows) and (0 <= c < n_cols) and not visit[r][c] and grid[r][c]):
            return

        visit[r][c] = True
        lands.add((r, c))
        for  n_r, n_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
            self.find_lands(grid, n_r, n_c, lands, visit)
