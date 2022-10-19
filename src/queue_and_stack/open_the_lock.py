"""
["0000"]
"8888"
"""
import heapq
from collections import defaultdict

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        blacklists = set(deadends)
        if '0000' in blacklists:
            return -1
        d = defaultdict(lambda : float('inf'))
        d['0000'] = 0
        heap = [(0, '0000')]
        
        while heap:
            dist, node = heapq.heappop(heap)
            
            if d[node] < dist:
                continue
            
            for i in range(4):
                digit = int(node[i])
                inc = (digit + 1) % 10
                dec = (digit + 10 - 1) % 10
                for change in [inc, dec]:
                    next_node = node[:i] + str(change) + node[i+1:]
                    if next_node not in blacklists and dist + 1 < d[next_node]:
                        d[next_node] = dist + 1
                        heapq.heappush(heap, (d[next_node], next_node))
                
        return d[target] if d[target] < float('inf') else -1
        
