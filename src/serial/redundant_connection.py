class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [-1] * n

        for a, b in edges:
            if self.is_same(a-1, b-1, par):
                return [a, b]
            self.unite(a-1, b-1, par)
        
    
    def find_root(self, node, par):
        if par[node] < 0:
            return node
        par[node] = self.find_root(par[node], par)
        return par[node]
    
    def is_same(self, a, b, par):
        return self.find_root(a, par) == self.find_root(b, par)
    
    def unite(self, a, b, par):
        if self.is_same(a, b, par):
            return
        
        root_a = self.find_root(a, par)
        root_b = self.find_root(b, par)

        if par[root_a] < par[root_b]:
            par[root_a] += par[root_b]
            par[root_b] = root_a
        else:
            par[root_b] += par[root_a]
            par[root_a] = root_b
