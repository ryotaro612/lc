"""
[[2,1,1],[2,3,1],[3,4,1]]
4
2

[[1,2,1]]
2
1

[[1,2,1]]
2
2
"""

import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = [float('inf')] * n
        g = [[] for _ in range(n)]
        
        for u, v, w in times:
            g[u-1].append([v-1, w])
        
        d[k-1] = 0
        heap = [[0, k-1]]
        
        while heap:
            dist, node = heapq.heappop(heap)
            if d[node] < dist:
                continue
                
            for next_node, w in g[node]:
                if d[node] + w < d[next_node]:
                    d[next_node] = d[node] + w
                    heapq.heappush(heap, [d[next_node], next_node])
        
        max_time = max(d)
        if max_time == float('inf'):
            return -1
        else:
            return max_time
