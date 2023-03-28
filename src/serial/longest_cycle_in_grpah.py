from collections import deque
"""
[49,29,24,24,-1,-1,-1,2,23,-1,44,47,52,49,9,31,40,34,-1,53,33,-1,2,-1,18,31,0,9,47,35,-1,-1,-1,-1,4,12,14,19,-1,4,4,43,25,11,54,-1,25,39,17,-1,22,44,-1,44,29,50,-1,-1]
"""
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        g = [[] for _ in range(n)]
        rev_g = [set() for _ in range(n)]
        for i, a in enumerate(edges):
            if a != -1:
                g[i].append(a)
                rev_g[a].add(i)

        que = deque()
        for i in range(n):
            if len(g[i]) + len(rev_g[i]) <= 1:
                que.append(i)

        while que:
            node = que.popleft()
            if g[node]:
                neighbor = g[node].pop()
                rev_g[neighbor].remove(node)
                if len(g[neighbor]) + len(rev_g[neighbor]) <= 1:
                    que.append(neighbor)
            if rev_g[node]:
                neighbor = next(iter(rev_g[node]))
                rev_g[node].remove(neighbor)
                g[neighbor].pop()
                if len(g[neighbor]) + len(rev_g[neighbor]) <= 1:
                    que.append(neighbor)
 
        visited = [False for _ in range(n)]
        result =  -1
        for i in range(n):
            if g[i]:
                result = max(result, self.count(i, g, visited))
        return result

    def count(self, node, g, visited):
        if visited[node]:
            return 0
        visited[node] = True
        return 1 + self.count(g[node][0], g, visited)
