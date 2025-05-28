
from collections import deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n1 = len(edges1) + 1
        tree1 = [[] for _ in range(n1)]
        for a, b in edges1:
            tree1[a].append(b)
            tree1[b].append(a)

        tree1_count = self.count(tree1, k)
        if k == 0:
            return tree1_count
            
        n2 = len(edges2) + 1
        tree2 = [[] for _ in range(n2)]
        for a, b in edges2:
            tree2[a].append(b)
            tree2[b].append(a)

        tree2_mx = max(self.count(tree2, k-1))
        
        return [e + tree2_mx for e in tree1_count]


    
    def count(self, g, k):
        n = len(g)

        que = deque()
        res = [0] * n
        for i in range(n):
            que.append([i, 0])
            visit = {i}
            while que:
                node, dist = que.popleft()
                if dist == k:
                    continue
                for succ in g[node]:
                    if succ in visit:
                        continue
                    
                    visit.add(succ)
                    que.append([succ, dist + 1])
            
            res[i] = len(visit)
        
        return res
