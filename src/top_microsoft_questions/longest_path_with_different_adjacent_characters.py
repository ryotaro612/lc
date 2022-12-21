class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        g = [[] for _ in range(n)]
        
        par = [-1] * n
        for node, p in enumerate(parent):
            if p != -1 and s[node] != s[p]:
                g[node].append(p)
                g[p].append(node)
                self.unite(node, p, par)

        roots = {self.find_root(node, par) for node in range(n)}
      
        result = 0
        for root in roots:
            result = max(result, self.find_sub_path(root, -1, g)[0])
        return result

    def find_sub_path(self, node, parent, g):
        if g[node] == [] or g[node] == [parent]:
            return [1, 1]
        
        result = 0
        paths = []

        for child in [c for c in g[node] if c != parent]:
            sub_result, longest_path = self.find_sub_path(child, node, g)
            result = max(result, sub_result, longest_path + 1)
            paths.append(longest_path + 1)
        paths = sorted(paths, reverse=True)
        if len(paths) > 1:
            result = max(result, paths[0] + paths[1] - 1)
        # print(node, parent, paths[0], result)
        return result, paths[0]
        

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
        
