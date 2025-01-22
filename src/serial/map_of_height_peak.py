from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n_rows = len(isWater)
        n_cols = len(isWater[0])
        grid = [[float('inf')] * n_cols for _ in range(n_rows)]
        que = deque([])
        for r in range(n_rows):
            for c in range(n_cols):
                if isWater[r][c] == 1:
                    grid[r][c] = 0
                    que.append([r,c])
        
        
        while que:
            r, c = que.popleft()

            for n_r, n_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
                if 0 <= n_r < n_rows and 0 <= n_c < n_cols:

                    if grid[n_r][n_c] > grid[r][c] + 1:
                        grid[n_r][n_c] = grid[r][c] + 1
                        que.append([n_r, n_c])
            
        return grid
