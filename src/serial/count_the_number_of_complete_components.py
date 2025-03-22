from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [-1] * n
        for a, b in edges:
            self.unite(a, b, par)
        
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        root_nodes = defaultdict(list)
        for v in range(n):
            root_nodes[self.find_root(v, par)].append(v)
        
        counter = 0

        for root, nodes in root_nodes.items():

            for node in nodes:
                if -par[self.find_root(root, par)] - 1 != len(g[node]):
                    break
            else:
                counter += 1
        
        return counter

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
