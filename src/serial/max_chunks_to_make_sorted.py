class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        par = [-1] * n

        for i, a in enumerate(arr):
            l, r = min(i, a), max(i, a)
            for v in range(l, r+1):
                self.unite(v, l, par)
        
        groups = set()
        for i in arr:
            groups.add(self.find_root(i, par))

        return len(groups)


    def find_root(self, n, par):
        if par[n] < 0:
            return n
        par[n] = self.find_root(par[n], par)
        return par[n]
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
            
