import bisect
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[True] * n for _ in range(m)]

        guards = {(r, c) for r, c in guards}
        walls = {(r, c) for r, c in walls}

        for r in range(m):
            self.traverse(grid, r, 0, 0, 1, guards, walls)
            self.traverse(grid, r, n-1, 0, -1, guards, walls)
        for c in range(n):
            self.traverse(grid, 0, c, 1, 0, guards, walls)
            self.traverse(grid, m-1, c, -1, 0, guards, walls)

        return len([e for row in grid for e in row if e])

    def traverse(self, grid, r, c, d_r, d_c, guards, walls):
        ok = True
        m = len(grid)
        n = len(grid[0])
        while 0 <= r < m and 0 <= c < n:
            if (r, c) in guards or (r, c) in walls:
                grid[r][c] = False
            
            if (r, c) in guards:
                ok = False
            if (r, c) in walls:
                ok = True
            
            grid[r][c] = grid[r][c] and ok
            r += d_r
            c += d_c
        
