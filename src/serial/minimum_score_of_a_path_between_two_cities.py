"""
16
[[6,10,2373],[2,12,9953],[12,3,8785],[3,2,1055],[11,1,4921],[6,11,5874],[11,3,1369],[3,16,1669],[16,11,9097],[1,6,9547],[12,11,2554],[10,11,5446],[4,11,4889],[10,4,8651],[4,12,4138]]
"""
from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        par = [-1 for _ in range(n)]
        for a, b, d in roads:
            self.unite(a-1, b-1, par)
        result = float('inf')
        for a, b, d in roads:
            if self.is_same_group(0, a-1, par):
                result = min(result, d)
        return result

    def find_root(self, a, par):
        if par[a] < 0:
            return a
        par[a] = self.find_root(par[a], par)
        return par[a]
    
    def is_same_group(self, a, b, par):
        return self.find_root(a, par) == self.find_root(b, par)

    def unite(self, a, b, par):
        if self.is_same_group(a, b, par):
            return
        
        root_a = self.find_root(a, par)
        root_b = self.find_root(b, par)
        if par[root_a] < par[root_b]:
            par[root_a] += par[root_b]
            par[root_b] = root_a
        else:
            par[root_b] += par[root_a]
            par[root_a] = root_b
