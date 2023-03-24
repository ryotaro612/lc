class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = [False for _ in range(n)]
        g = [[] for _ in range(n)]
        rev_g = [[] for _ in range(n)]
        for start, end in connections:
            g[start].append(end)
            rev_g[end].append(start)
        
        return self.traverse(0, visited, g, rev_g)

    def traverse(self, node, visited, g, rev_g):
        visited[node] = True
        result = 0
        for neighbor in g[node]:
            if not visited[neighbor]:
                result += 1
                result += self.traverse(neighbor, visited, g, rev_g)
        for neighbor in rev_g[node]:
            if not visited[neighbor]:
                result += self.traverse(neighbor, visited, g, rev_g)
        return result 
        
