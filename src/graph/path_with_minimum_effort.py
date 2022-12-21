"""
[[1,2,2],[3,8,2],[5,3,5]]
[[1,2,3],[3,8,4],[5,3,5]]
[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
"""
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n_row = len(heights)
        n_col = len(heights[0])
        
        d = [float('inf')] * (n_row * n_col)
        d[0] = 0
        heap = [[0, 0]]
        while heap:
            dist, node = heapq.heappop(heap)
            
            r = node // n_col
            c = node % n_col
            
            for next_r, next_c in [[r-1, c], [r, c+ 1], [r+1, c], [r, c-1]]:
                if 0 <= next_r < n_row and 0 <= next_c < n_col:
                    next_node = next_r * n_col + next_c
                    new_dist = max(d[node], abs(heights[r][c] - heights[next_r][next_c]))
                    if d[next_node] > new_dist:
                        d[next_node] = new_dist
                        heapq.heappush(heap, [new_dist, next_node])
        
        return d[-1]
