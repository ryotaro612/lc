
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visit = set()
        res = [None] * len(graph)

        for node in range(len(graph)):
            if res[node] is None:
                self.rec(node, graph, res, visit)

        return [v for v in range(len(graph)) if res[v]]

    def rec(self, node, graph, res, visit):
        if res[node] is not None:
            return res[node]

        if node in visit:
            res[node] = False
            return False
 
        visit.add(node)
        ok = True
        for neigh in graph[node]:
            ok = ok and self.rec(neigh, graph, res, visit)
        res[node] = ok
        return res[node] 
