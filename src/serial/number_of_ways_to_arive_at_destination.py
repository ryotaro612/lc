import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        time 
        time + a
        a
        counter = 0
        for succ for successors:
            couter += self.rec(succ)
        
        return couter
        """
        g = [[] * n for _ in range(n)]
        for a, b, time in roads:
            g[a].append([b, time])
            g[b].append([a, time])

        d = [float('inf')] * n
        d[0] = 0
        # (time, node)
        heap = [(0, 0)]

        while heap:
            time, node = heapq.heappop(heap)
            if d[node] < time:
                continue
            
            for succ, succ_time in g[node]:
                cand = d[node] + succ_time
                if d[succ] > cand:
                    d[succ] = cand
                    heapq.heappush(heap, (cand, succ))
        
        cache = dict()
        return self.rec(0, d, g, cache)
    
    def rec(self, node, d, g, cache):
        if node in cache:
            return cache[node]

        if node == len(d) - 1:
            cache[node] = 1
            return 1
        
        counter = 0
        for succ, time in g[node]:
            if d[succ] == d[node] + time:
                counter += self.rec(succ, d, g, cache)

        cache[node] = counter % (10**9 + 7)
        return cache[node]
