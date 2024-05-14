class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])

        result = 0
        for r in range(n_rows):
            for c in range(n_cols):
                visit = set()
                visit.add((r, c))
                result = max(result, self.traverse(r, c, grid, visit))
                visit.remove((r, c))

        return result
    
    def traverse(self, r, c, grid, visit):
        if grid[r][c] == 0:
            return 0
        
        n_rows = len(grid)
        n_cols = len(grid[0])

        result = grid[r][c]
 
        for adj_r, adj_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
            if 0 <= adj_r < n_rows and 0 <= adj_c < n_cols and (adj_r, adj_c) not in visit:
                visit.add((adj_r, adj_c))
                result = max(result, grid[r][c] + self.traverse(adj_r, adj_c, grid, visit))
                visit.remove((adj_r, adj_c))
                
        return result
    
