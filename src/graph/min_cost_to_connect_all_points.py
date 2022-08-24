# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         if n == 1:
#             return 0
#         d = []
#         for i in range(n-1):
#             for j in range(i+1, n):
#                 dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
#                 d.append((dist, i, j))
#         d.sort()
        
#         par = [-1] * n
#         result = 0
#         for dist, i, j in d:
#             if not self.isSame(i, j, par):
#                 result += dist
#                 self.unite(i, j, par)
#         return result
        
#     def findRoot(self, a, par):
#         if par[a] < 0:
#             return a
#         par[a] = self.findRoot(par[a], par)
#         return par[a]
    
#     def isSame(self, a, b, par):
#         return self.findRoot(a, par) == self.findRoot(b, par)
    
#     def unite(self, a, b, par):
#         if self.isSame(a, b, par):
#             return
        
#         root_a = self.findRoot(a, par)
#         root_b = self.findRoot(b, par)
        
#         if par[root_a] < par[root_b]:
#             par[root_a] += par[root_b]
#             par[root_b] = root_a
#         else:
#             par[root_b] += par[root_a]
#             par[root_a] = root_b

import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        que = []
        for i in range(1, n):
            dist = abs(points[0][0] - points[i][0]) + abs(points[0][1] - points[i][1])
            que.append((dist, i))
        used = [False] * n
        used[0] = True
        result = 0
        heapq.heapify(que)
        
        while que:
            dist, a = heapq.heappop(que)
            if used[a]:
                continue
            used[a] = True
            result += dist
            for i in range(n):
                if a != i and not used[i]:
                    dist = abs(points[i][0] - points[a][0]) + abs(points[i][1] - points[a][1])
                    heapq.heappush(que, (dist, i))
        return result
    
