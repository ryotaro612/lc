import heapq
from collections import deque

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        d = [float('inf')] * n
        g = [[] for _ in range(n)]
        for a, b, w in edges:
            g[a].append([b, w])
            g[b].append([a, w])
        d[0] = 0
        while heap:
            w, node = heapq.heappop(heap)
            if d[node] < w:
                continue
            
            for neighbor, n_w in g[node]:
                cost = d[node] + n_w
                if d[neighbor] > cost:
                    d[neighbor] = cost
                    heapq.heappush(heap, [d[neighbor], neighbor])
        
        if d[n-1] == float('inf'):
            return [False] * len(edges)
        
        passed = set()
        que = deque([n - 1])
        while que:
            node = que.popleft()
            for neighbor, w in g[node]:
                if d[node] - d[neighbor] == w and (neighbor, node) not in passed:
                    passed.add((neighbor, node))
                    que.append(neighbor)  
        
        result = [False] * len(edges)
        for i, [a, b, w] in enumerate(edges):
            if (a, b) in passed or (b, a) in passed:
                result[i] = True
        return result
