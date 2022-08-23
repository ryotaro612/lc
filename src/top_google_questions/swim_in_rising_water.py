import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        times = [[-1] * n for _ in range(n)]
        
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        t = 0
        while len(heap) > 0:
            _, r, c = heapq.heappop(heap)
            if t < grid[r][c]:
                t = grid[r][c]
            times[r][c] = t
            for next_r, next_c in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                if 0 <= next_r < n and 0<=next_c< n and times[next_r][next_c] < 0:
                    heapq.heappush(heap, (grid[next_r][next_c], next_r, next_c))
        
        #for row in times:
        #    print(row)
        return times[n-1][n-1]
    
