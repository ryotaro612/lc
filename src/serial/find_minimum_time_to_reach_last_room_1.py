import heapq

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n_rows = len(moveTime)
        n_cols = len(moveTime[0])
        d = [[float('inf')] * n_cols for _ in range(n_rows)]
        d[0][0] = 0
        # distance, row, col
        heap = [(0, 0, 0)]

        while heap:
            dist, r, c = heapq.heappop(heap)

            if d[r][c] < dist:
                continue
            
            for s_r, s_c in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                if 0 <= s_r < n_rows and 0 <= s_c < n_cols:
                    cost = 1 + max(moveTime[s_r][s_c], d[r][c])
                    if cost < d[s_r][s_c]:
                        d[s_r][s_c] = cost
                        heapq.heappush(heap, (cost, s_r, s_c))
        
        return d[n_rows-1][n_cols-1]
