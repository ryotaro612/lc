from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """
        sum(min(0, m - (n-1)))
        n_groups

        return n_groups - 1 <= redundant_edges
        """
        par = [-1 for _ in range(n)]
        for a, b in connections:
            self.unite(a, b, par)

        group_nodes = defaultdict(set)
        for node in range(n):
            group = self.find_root(node, par)
            group_nodes[group].add(node)

        group_n_edges = defaultdict(int)
        for a, b in connections:
            group = self.find_root(a, par)
            group_n_edges[group] += 1
        
        redundant = 0
        for group in group_nodes:
            redundant += max(0, group_n_edges[group] - (len(group_nodes[group]) -1))
        
        if redundant < len(group_nodes) - 1:
            return -1
        return len(group_nodes) - 1

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
