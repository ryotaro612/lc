from collections import defaultdict
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]

        for a, b, w in edges:
            g[a].append([b, w])
            g[b].append([a, w])
        
        cache = {}
        result = []
        for node in range(n):
            counters = []
            for child, w in g[node]:
                counter = self.rec(child, node, g, cache)

                freq = 0
                for k, v in counter.items():
                    if (k + w) % signalSpeed == 0:
                        freq += v
                
                counters.append(freq)

            total = sum(counters)
            res = 0
            for counter in counters:
                res += counter * (total-counter)

            result.append(res // 2)
        return result
    def rec(self, node, parent, g, cache):
        if (node, parent) in cache:
            return cache[(node, parent)]
        # weight-> number
        counter = defaultdict(int)
        counter[0] += 1
        for child, w in g[node]:
            if child == parent:
                continue

            for k, v in self.rec(child, node, g, cache).items():
                counter[w + k] += v
        
        cache[(node, parent)] = counter
        return counter
            
