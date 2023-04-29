
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        par = [-1] * n

        edgeList.sort(key=lambda triple: triple[2])
        edge_i = 0
        result = [False] * len(queries)
        index_queries = sorted([[i] + query for i, query in enumerate(queries)], key=lambda e: e[3])
        for query_i, p, q, limit in index_queries:
            while len(edgeList) > edge_i and edgeList[edge_i][2] < limit:
                self.unite(edgeList[edge_i][0], edgeList[edge_i][1], par)
                edge_i += 1
            if self.is_same_group(p, q, par):
                result[query_i] = True
        return result

    def find_root(self, i, par):
        if par[i] < 0:
            return i
        par[i] = self.find_root(par[i], par)
        return par[i]

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
