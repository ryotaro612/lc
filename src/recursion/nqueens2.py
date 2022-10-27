class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [[True] * n for _ in range(n)]
        return self.solve(0, 0, n, grid)
    
    def solve(self, r, c, count, grid):
        if count == 0:
            return 1
        n = len(grid)
        if not ((0 <= r < n) and (0 <= c < n)):
            return 1 if count == 0 else 0 
        
        if c == n-1:
            result = self.solve(r+1, 0, count, grid)
        else:
            result = self.solve(r, c+1, count, grid) 
        
        if grid[r][c]:
            revert = []
            for i in range(r, n):
                if grid[i][c]:
                    grid[i][c] = False
                    revert.append((i, c))
            n_r = r
            n_c = c
            while 0 <= n_r < n and 0 <= n_c < n:
                if grid[n_r][n_c]:
                    grid[n_r][n_c] = False
                    revert.append((n_r, n_c))
                n_r += 1
                n_c += 1
            
            n_r = r
            n_c = c
            while 0 <= n_r < n and 0<=n_c < n:
                if grid[n_r][n_c]:
                    grid[n_r][n_c] = False
                    revert.append((n_r, n_c))
                n_r += 1
                n_c -= 1
            
            result += self.solve(r+1, 0, count - 1, grid)
            for a, b in revert:
                grid[a][b] = True
        return result
        
