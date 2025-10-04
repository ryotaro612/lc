from collections import defaultdict

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        """
        i + k
        0 , k,  2k
        1, k + 1, 2k + 1, ..
        
        0,..k-1
        1,...k

        sum // n_g or sum // n_g + 1
        """
        result = 0
        n = len(arr)
        par = [-1] * n

        for i in range(k):
            j = i
            while j < n:
                self.unite(j, (j+k) % n, par)
                j += k
        group_map = defaultdict(list)
        for i in range(n):
            group_map[self.find_root(i, par)].append(arr[i])

        for group in group_map.values():
            # print(group)
            group.sort()            
            n_g = len(group)
            total = sum(group)
            target = total // n_g
            cand = 0
            cand2 = 0
            cand3 = 0 
            cand4 = 0
            for e in group:
                cand += abs(e - target)
                cand2 += abs(e - (target + 1))
                cand3 += abs(e - group[n_g //2])
                cand4 += abs(e - group[n_g//2 + 1 if n_g -1 > n_g//2 + 1 else n_g//2])
            result += min(cand, cand2, cand3, cand4)
        
        return result
    
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
