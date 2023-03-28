class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        par = [-1 for _ in range(n)]
        for a, b in edges:
            self.unite(a, b, par)
        
        result = 0
        for i in range(n):
            result += n - self.count(i, par)

        return result // 2
        
    def count(self, a, par):
        return -par[self.find_root(a, par)]
    
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
