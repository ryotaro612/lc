from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        d = [[[float('inf')] * (k+1) for _ in range(n_col)]  for _ in range(n_row)]
        
        que = deque()
        que.append((0, 0, 0, 0))
        d[0][0][0] = 0
        while len(que) > 0:
            r, c, dist, elim = que.popleft()
            
            if d[r][c][elim] < dist:
                continue
                
            for next_r, next_c in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                if 0<=next_r<n_row and 0<= next_c < n_col:
                    if grid[next_r][next_c] == 0:

                        if dist + 1 < d[next_r][next_c][elim]:
                            d[next_r][next_c][elim] = dist + 1
                            que.append((next_r, next_c, dist+1, elim))
                    else:
                        if elim < k and dist + 1 < d[next_r][next_c][elim+1]:
                            d[next_r][next_c][elim+1] = dist + 1
                            que.append((next_r, next_c, dist+1, elim+1))
        #for e in d:
        #    print(e)
        result = min(d[n_row-1][n_col-1])                    
        if result == float('inf'):
            return -1
        return result
