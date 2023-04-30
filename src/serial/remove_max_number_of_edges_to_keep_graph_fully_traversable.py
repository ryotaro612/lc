class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        par_a = [-1] * n
        par_b = [-1] * n

        res = 0
        for t, u, v in sorted(
            [[t, u - 1, v - 1] for t, u, v in edges], key=lambda edge: -edge[0]
        ):
            add = False
            if t in {3, 1}:
                if not self.is_same_group(u, v, par_a):
                    self.unite(u, v, par_a)
                    add = True
            if t in {3, 2}:
                if not self.is_same_group(u, v, par_b):
                    self.unite(u, v, par_b)
                    add = True
            if add:
                res += 1
        if min(-par_b[self.find_root(0, par_b)], -par_a[self.find_root(0, par_a)]) < n:
            return -1
        return len(edges) - res

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
