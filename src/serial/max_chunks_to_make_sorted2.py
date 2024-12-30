class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        tuples = sorted([[a, i] for i, a in enumerate(arr)])
        order = [0] * n
        for i, [_, j] in enumerate(tuples):
            order[j] = i

        par = [-1] * n 
        for i in range(n):
            for a in range(order[i], i - 1, -1):
                if i < a:
                    if self.is_same(i, a, par):
                        break
                self.unite(a, i, par)
        
        return len({self.find_root(i, par) for i in range(n)})

    
    def find_root(self, i, par):
        if par[i] < 0:
            return i
        par[i] = self.find_root(par[i], par)
        return par[i]
    
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
