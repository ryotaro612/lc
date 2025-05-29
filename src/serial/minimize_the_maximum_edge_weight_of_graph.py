import heapq

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        ub = 1000002
        lb = 0

        rev_g = [[] for _ in range(n)]
        for a, b, w in edges:
            rev_g[b].append([a, w])

        while ub - lb > 1:
            mid = (ub+lb) // 2
            visit = {0}
            self.check(rev_g, 0, visit, mid)    
            if len(visit) < n:
                lb  = mid
            else:
                ub = mid
        
        return ub if ub < 1000001 else -1

    def check(self, g, node, visit, pivot):
        
        for succ, w in g[node]:
            if w <= pivot and succ not in visit:
                visit.add(succ)
                self.check(g, succ, visit, pivot)

                
