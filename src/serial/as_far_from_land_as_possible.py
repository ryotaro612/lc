from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        d = [[float('inf')] * n_col for _ in range(n_row + 1)]
        que = deque()
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c]:
                    d[r][c] = 0
                    que.append([0, r, c])
        
        if len(que) in {0, n_col * n_row}:
            return -1

        result=0
        while que:
            cost, r, c = que.popleft()
            if d[r][c] < cost:
                continue
            for n_r, n_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
                if 0 <= n_r < n_row and 0 <= n_c < n_col and 1 + cost < d[n_r][n_c]:
                    d[n_r][n_c] = 1 + cost
                    result = max(result, d[n_r][n_c])
                    que.append([1+cost, n_r, n_c])
        return result

