class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        """
        b, a, c
        c, a, c
        d, d, c
        b, c, c
        """
        n_rows = len(grid)
        n_cols = len(grid[0])
        visit = [[False] * n_cols for _ in range(n_rows)]
        for r in range(n_rows):
            for c in range(n_cols):
                if visit[r][c]:
                    continue
                visit[r][c] = True
                if self.traverse(r, c, -1, -1, visit, grid):
                    
                    return True
        
        return False
    
    def traverse(self, r, c, prev_r, prev_c, visit, grid):
        n_rows = len(visit)
        n_cols = len(visit[0])

        for s_r, s_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
            if 0 <= s_r < n_rows and 0 <= s_c < n_cols and (s_r, s_c) != (prev_r, prev_c) and grid[r][c] == grid[s_r][s_c]:
                if visit[s_r][s_c]:
                    return True
                visit[s_r][s_c] = True
                if self.traverse(s_r, s_c, r, c, visit, grid):
                    return True
        
        return False


