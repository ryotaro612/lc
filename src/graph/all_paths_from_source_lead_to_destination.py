"""
3
[[0,1],[0,2]]
0
2

4
[[0,1],[0,3],[1,2],[2,1]]
0
3

4
[[0,1],[0,2],[1,3],[2,3]]
0
3

3
[[0,1],[1,1],[1,2]]
0
2

5
[[0,1],[1,2],[2,3],[3,4]]
1
3
"""
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for start, end in edges:
            if start == destination:
                return False
            g[start].append(end)
        reachable = [None] * n
        result = self.find(source, set(), reachable, destination, g)
        return result
    def find(self, node, visited, reachable, destination, g):
        #print(node)
        if node in g[node]:
            reachable[node] = False
            return False
        if destination == node:
            reachable[node] = True
            return True

        visited.add(node)
        neighbors = [neigh for neigh in g[node] if neigh not in visited]
        if neighbors:
            reachable[node] = True
            for neigh in neighbors:
                if reachable[neigh] is False:
                    reachable[node] = False
                elif reachable[neigh] is None:
                    reachable[node] = reachable[node] and self.find(
                        neigh, visited, reachable, destination, g)
        else:
            reachable[node] = False
        
        visited.remove(node)
        return reachable[node]
