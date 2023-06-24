"""
[[0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0],
 [0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0],
 [0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,1,0,0,1,0,0,1,0],
 [1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,1,1,1,1,1]]

"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        visit = [[False] * n_col for _ in range(n_row)]
        result = set()
        for r in range(n_row):
            for c in range(n_col):
                if visit[r][c] or not grid[r][c]:
                    continue
                path = [[r, c]]
                visit[r][c] = True
                self.travel(r, c, grid, visit, path)
                path.sort()
                result.add(str(['%s' % [item[0] - path[0][0], item[1] - path[0][1]] for item in path]))    
        return len(result)
    
    def travel(self, r, c, grid, visit, path):
        n_row, n_col = len(grid), len(grid[0])
        for n_r, n_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
            if 0 <= n_r < n_row and 0 <= n_c < n_col and not visit[n_r][n_c] and grid[n_r][n_c]:
                visit[n_r][n_c] = True
                path.append([n_r, n_c])
                self.travel(n_r, n_c, grid, visit, path)
            
