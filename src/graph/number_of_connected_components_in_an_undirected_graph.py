"""
4
[[2,3],[1,2],[1,3]]
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [-1] * n
        for a, b in edges:
            self.unite(a, b, par)
        groups = set()
        for node in range(n):
            groups.add(self.findRoot(node, par))
        return len(groups)
    
    def findRoot(self, i, par):
        if par[i] < 0:
            return i
        else:
            par[i] = self.findRoot(par[i], par)
            return par[i]
    
    def isSame(self, a, b, par):
        return self.findRoot(a, par) == self.findRoot(b, par)
    
    def unite(self, a, b, par):
        if self.isSame(a, b, par):
            return 
        
        root_a = self.findRoot(a, par)
        root_b = self.findRoot(b, par)
        if par[root_a] < par[root_b]:
            par[root_a] += par[root_b]
            par[root_b] = root_a
        else:
            par[root_b] += par[root_a]
            par[root_a] = root_b
