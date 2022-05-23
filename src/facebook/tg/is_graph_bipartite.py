class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # color[i] = None or False or True
        n = len(graph)
        colors = [None for _ in range(n)]
        
        for node in range(n):
            if colors[node] is None:
                colors[node] = False
            if not self.colorNode(graph, colors, node):
                return False
        return True
    
    def colorNode(self, graph, colors, node):
        
        for neighbor in graph[node]:
            if colors[neighbor] is None:
                colors[neighbor] = not colors[node]
                if not self.colorNode(graph, colors, neighbor):
                    return False
            else:
                if colors[node] == colors[neighbor]:
                    return False
        return True
                    
