"""
[1,3,2,1,3]
[[0,1],[0,2],[2,3],[2,4]]
"""
from collections import defaultdict, deque, Counter

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        g = [[] for _ in range(n)]
        for node1, node2 in edges:
            g[node1].append(node2)
            g[node2].append(node1)
        
        
        val_nodes = defaultdict(list)
        
        for i, v in enumerate(vals):
            val_nodes[v].append(i)
            
        result = n
        par = [-1] * n
        for v in sorted(val_nodes):
            for node in val_nodes[v]:
                
                for neighbor in g[node]:
                    if vals[neighbor] <= vals[node]:
                        self.unite(neighbor, node, par)
            
            group = Counter([self.find_root(node, par) for node in val_nodes[v]])
            for freq in group.values():
                result += freq * (freq-1) // 2
        
        return result
                
                        
    def find_root(self, i, par):
        if par[i] < 0:
            return i
        else:
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
    
            
