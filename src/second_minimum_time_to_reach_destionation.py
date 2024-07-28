import heapq

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        g = [[] for _ in range(n)]

        for a, b in edges:
            g[a-1].append(b-1)
            g[b-1].append(a-1)
        
        d = [float('inf')] * (2*n)
        d[0] = 0
        heap = []
        heapq.heappush(heap, [0, 0])

        while heap:
            dist, node = heapq.heappop(heap)
            if d[node] < dist:
                continue
            if dist // change % 2:
                dist += change - dist % change
            
            if node < n:
                neighbors = g[node]
            else:
                neighbors = g[node-n]
            # print(dist, node, neighbors)
            for neg in neighbors:
                if dist + time < d[neg]:
                    if d[neg] < d[neg+n]:
                        d[neg+n] = d[neg]
                        heapq.heappush(heap, [d[neg+n], neg+n])
                    d[neg] = dist + time
                    heapq.heappush(heap, [d[neg], neg])
                elif d[neg] < dist + time < d[neg+n]:
                    d[neg+n] = dist + time
                    heapq.heappush(heap, [d[neg+n], neg+n])
        # print(d[n-1])
        return d[2*n-1]
                
