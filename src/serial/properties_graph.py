class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        """
        1000000
        """
        n = len(properties)
        par = [-1] * n
        for i in range(n):
            for j in range(i+1, n):
                if len(set(properties[i]) & set(properties[j])) >= k:
                    self.unite(i, j, par)
        
        return len({self.find_root(a, par) for a in range(n)})
    
    def find_root(self, a, par):
        if par[a] < 0:
            return a
        par[a] = self.find_root(par[a], par)
        return par[a]
    
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
