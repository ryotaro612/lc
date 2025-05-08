import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n_rows = len(moveTime)
        n_cols = len(moveTime[0])
        heap = []
        d = [[[float('inf')]*2 for _ in range(n_cols)] for _ in range(n_rows)]
        d[0][0][0]=0
        # cost, step, row, col
        heap = [(0, 0, 0, 0)]
        
        while heap:
            cost, step, r, c = heapq.heappop(heap)
            if d[r][c][step] < cost:
                continue
            
            next_step = 0 if step else 1
            for s_r, s_c in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                if 0<= s_r < n_rows and 0 <= s_c < n_cols:
                    next_cost = 2 if step else 1
                    next_cost += max(moveTime[s_r][s_c], d[r][c][step])

                    if next_cost < d[s_r][s_c][next_step]:
                        d[s_r][s_c][next_step] = next_cost
                        heapq.heappush(heap, (next_cost, next_step, s_r, s_c))
            
        return min(d[n_rows-1][n_cols-1])
