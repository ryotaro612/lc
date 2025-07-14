class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        """
        g
        """
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        found = {0}
        restricted = set(restricted)

        self.visit(0, -1, g, found, restricted)
        
        return len(found)
    
    def visit(self, node, parent, g, found, restricted):
        
        for child in g[node]:
            if child in restricted or child == parent:
                continue
            
            found.add(child)
            self.visit(child, node, g, found, restricted)
        
