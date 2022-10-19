"""
[[0,0,0],
 [1,0,0],
 [1,1,0]]
"""
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        
        n = len(grid)
        que = deque()
        d = [float('inf')] * (n*n)
        d[0] = 0
        que.append((0, 0))
        
        while que:
            cost, node = que.popleft()
            # print('node', node, cost)
            if d[node] < cost:
                continue
            
            r = node // n
            c = node % n
            
            for (next_r, next_c) in [
                (r-1, c), (r, c+1), (r+1, c), (r, c-1), (r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]:
                if 0 <= next_r < n and 0 <= next_c < n and grid[next_r][next_c] == 0:
                    indice = next_r * n + next_c
                    if cost + 1 < d[indice]:
                        d[indice] = cost + 1
                        #print('append', indice, cost + 1)
                        que.append((cost + 1, indice))
        #print(d)
        if d[n*n-1] == float('inf'):
            return -1
        else:
            return d[n*n-1] +  1
