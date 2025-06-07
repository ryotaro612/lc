import heapq

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        n_rows = len(grid)
        n_cols = len(grid[0])
        d = [[float('inf')] * n_cols for _ in range(n_rows)]
        heap = []

        for c in range(n_cols):
            d[0][c] = grid[0][c]
            heapq.heappush(heap, (d[0][c], 0, c))
        
        while heap:
            cost, r, c = heapq.heappop(heap)
            if r == n_rows - 1 or cost > d[r][c]:
                continue
            
            for s_c in range(n_cols):
                next_cost = d[r][c] + grid[r+1][s_c] + moveCost[grid[r][c]][s_c]
                if next_cost < d[r+1][s_c]:
                    d[r+1][s_c] = next_cost
                    heapq.heappush(heap, (d[r+1][s_c], r+1, s_c))
                
        return min(d[-1])
            
