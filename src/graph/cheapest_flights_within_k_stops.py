"""
4
[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
0
3
1

3
[[0,1,100],[1,2,100],[0,2,500]]
0
2
1

5
[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
0
2
2

4
[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
0
3
1
"""
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = [[float('inf')] * (n+2) for _ in range(n)]
        
        g = [[] for _ in range(n)]
        for start, end, cost in flights:
            g[start].append([end, cost])
        
        heap = []
        d[src][0] = 0
        heapq.heappush(heap, [0, src, 0])
        
        while heap:
            dist, node, n_stops = heapq.heappop(heap)
            
            if d[node][n_stops] < dist:
                continue
                
            for end, cost in g[node]:
                if n_stops <= k and d[end][n_stops + 1] > dist + cost:
                    d[end][n_stops + 1] = dist + cost
                    heapq.heappush(heap, [d[end][n_stops + 1], end, n_stops + 1])
        
        result = min(d[dst][:k+2])
        if result == float('inf'):
            return -1
        else:
            return result
