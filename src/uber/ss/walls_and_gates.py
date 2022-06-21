"""
0 inf inf inf
0 inf inf inf
0 inf inf inf 
"""
import heapq
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        spaces = []
        n = len(rooms)
        m = len(rooms[0])
        for r in range(n):
            for c in range(m):
                if rooms[r][c] == 0:
                    spaces.append((0, r, c))
        heapq.heapify(spaces)
        
        while len(spaces) > 0:
            d, r, c = heapq.heappop(spaces)
            if rooms[r][c] < d:
                continue
            candidates = [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]
            for next_r, next_c in candidates:
                if 0 <= next_r and next_r < n and 0 <= next_c and next_c < m:
                    if rooms[next_r][next_c] != -1:
                        if d + 1 < rooms[next_r][next_c]:
                            rooms[next_r][next_c] = d + 1
                            heapq.heappush(spaces, (d+1, next_r, next_c))
                    
         
