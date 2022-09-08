class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        
        self.rec(0, [], set(), result, graph)
        
        return result
    
    def rec(self, node, path, visited, result, graph):
        n = len(graph)
        if node  == n - 1:
            result.append(path + [node])
            return
        
        visited.add(node)
        path.append(node)
        for next_node in graph[node]:
            if next_node not in visited:
                self.rec(next_node, path, visited, result, graph)
        visited.remove(node)
        path.pop()
