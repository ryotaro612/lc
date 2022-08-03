class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        par = [-1 for _ in range(n)]
        
        for [a, b] in edges:
            if self.isSame(a, b, par):
                return False
            else:
                self.unite(a, b, par)
        return True
        
    def findRoot(self, i, par):
        if par[i] < 0:
            return i
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
