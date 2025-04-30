class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        return self.count(g, 0, -1, hasApple)


    def count(self, g, node, parent, has_apple):
        result = 0
        
        for child in g[node]:
            if parent == child:
                continue
            
            sub = self.count(g, child, node, has_apple)
            result += sub
            if sub or has_apple[child]:
                result += 2
        return result


                
