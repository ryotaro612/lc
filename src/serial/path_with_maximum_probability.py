import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = defaultdict(list)
        for i, [a, b] in enumerate(edges):
            prob = succProb[i]
            g[a].append([prob, b])
            g[b].append([prob, a])

        d = [float('inf')] * n
        d[start] = 0
        heap = [[0, start]]

        while heap:
            prob, node = heapq.heappop(heap)
            if d[node] < prob:
                continue
            
            for edge_prob, neighbor in g[node]:
                cand = 1 - (1 - d[node]) * edge_prob
                if d[neighbor] > cand:
                    d[neighbor] = cand
                    heapq.heappush(heap, [cand, neighbor])
        if d[end] > 1:
            return 0
        else:
            return 1 - d[end]
