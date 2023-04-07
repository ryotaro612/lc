from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n_row, n_col = len(grid), len(grid[0])
        visit = [[False] * n_col for _ in range(n_row)]

        que = deque()
        for r, c in [(a, b) for b in range(n_col) for a in [0, n_row-1]] + [(a, b) for a in range(n_row) for b in [0, n_col-1]]:
            que.append((r, c))
            while que:
                r, c = que.pop()
                if 0 <= r < n_row and 0 <= c < n_col and not visit[r][c] and grid[r][c]:
                    visit[r][c] = True
                    que.extend([(r-1, c), (r, c+1), (r+1, c), (r, c-1)])

        return len([(r, c) 
                    for r in range(n_row) 
                    for c in range(n_col) 
                    if grid[r][c] and not visit[r][c]])
