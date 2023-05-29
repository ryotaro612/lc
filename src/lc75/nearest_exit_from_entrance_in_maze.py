from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n_row = len(maze)
        n_col = len(maze[0])
        
        d = [float('inf')] * (n_row * n_col)
        d[entrance[0] * n_col + entrance[1]] = 0
        que = deque()
        que.append(entrance)
        while que:
            r, c = que.popleft()

            for n_r, n_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
                if not (0<= n_r < n_row and 0 <= n_c < n_col) or maze[n_r][n_c] == '+':
                    continue
                i = n_r * n_col + n_c
                dist = d[r*n_col + c] + 1
                if d[i] > dist:
                    d[i] = dist
                    que.append([n_r, n_c])
        
        result = float('inf')
        for r, c in [[r, c] for r in [0, n_row-1] for c in range(n_col)] + [[r, c] for c in [0, n_col-1] for r in range(n_row)]:
            if [r, c] != entrance:
                result = min(result, d[r*n_col + c])
        
        if result < float('inf'):
            return result
        else:
            return -1
