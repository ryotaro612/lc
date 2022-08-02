"""
10
[[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
5
9
"""
from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = defaultdict(list)
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)
            
        d = [float('inf')] * n
        
        que = deque()
        print(g)
        d[source] = 0
        que.append((0, source))
        while len(que):
            dist, node = que.popleft()
            if dist > d[node]:
                continue
                
            for neigh in g[node]:
                if d[node] + 1 < d[neigh]:
                    d[neigh] = d[node] + 1
                    que.append((d[neigh], neigh))
        # print(d)            
        return d[destination] < float('inf')
