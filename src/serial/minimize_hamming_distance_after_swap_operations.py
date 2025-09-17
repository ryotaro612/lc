from collections import defaultdict

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        """
        [0, 1], [1, 2] -> 
        root-> {source_val: freq}
        """
        n = len(source)
        par = [-1] * n

        for a, b in allowedSwaps:
            self.unite(par, a, b)
        
        freq = defaultdict(lambda: defaultdict(int))

        for i, v in enumerate(source):
            freq[self.find_root(par, i)][v] += 1
        
        result = 0

        for i, v in enumerate(target):
            root = self.find_root(par, i)
            if freq[root][v]:
                freq[root][v] -= 1
            else:
                result += 1
        
        return result

    def find_root(self, par, idx):
        if par[idx] < 0:
            return idx
        par[idx] = self.find_root(par, par[idx])
        return par[idx]

    def is_same(self, par, a, b):
        return self.find_root(par, a) == self.find_root(par, b)

    def unite(self, par, a, b):
        if self.is_same(par, a, b):
            return

        root_a = self.find_root(par, a)
        root_b = self.find_root(par, b)

        if par[root_a] < par[root_b]:
            par[root_a] += par[root_b]
            par[root_b] = root_a
        else:
            par[root_b] += par[root_a]
            par[root_a] = root_b
                
