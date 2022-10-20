"""

(1/ack)(len_of_airs) + num_groups * (max_size_of_group log max_size_of_group) + n

"dcab"
[[0,3],[1,2],[0,2]]

"dcab"
[]
"""
from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        par = [-1] * n
        groups = defaultdict(set)
        for pos1, pos2 in pairs:
            self.unite(pos1, pos2, par)
        for pos1, pos2 in pairs:
            group = self.find_root(pos1, par)
            groups[group].update([(s[pos1], pos1), (s[pos2], pos2)])
        
        result = [c for c in s]
        
        for group in groups:
            chars = sorted([c for c, _ in groups[group]])
            positions = sorted([p for _, p in groups[group]])
            for pos, char in zip(positions, chars):
                result[pos] = char
            
            
        return ''.join(result)
        
    def find_root(self, a, par):
        if par[a] < 0:
            return a;
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
