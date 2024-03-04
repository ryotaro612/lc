import heapq

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        
        d = [[float('inf')] * len(ring) for _ in range(len(key) + 1)]
        d[0][0] = 0
        heap = [[d[0][0], 0, 0]]
        
        while heap:
            cost, n_processed, dial_pos = heapq.heappop(heap)
            
            if d[n_processed][dial_pos] < cost or n_processed == len(key):
                continue
        
            if key[n_processed] == ring[dial_pos]:
                new_dist = d[n_processed][dial_pos] + 1
                if d[n_processed+1][dial_pos] > new_dist:
                    d[n_processed+1][dial_pos] = new_dist
                    heapq.heappush(heap, [new_dist, n_processed+1, dial_pos])
            
            for p in [(dial_pos + 1) % len(ring), (dial_pos - 1 + len(ring)) % len(ring)]:
                new_dist = d[n_processed][dial_pos] + 1
                if d[n_processed][p] > new_dist:
                    d[n_processed][p] = new_dist
                    heapq.heappush(heap, [new_dist, n_processed, p])
                    
        return min([v for v in d[len(key)]])
