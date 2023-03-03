"""
4
[[0,1],[2,3],[1,3]]
[[1,2]]

6
[[4,1],[3,5],[5,2],[1,4],[4,2],[0,0],[2,0],[1,1]]
[[5,5],[5,0],[4,4],[0,3],[1,0]]
"""
from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = [set() for _ in range(n)]
        blue = [set() for _ in range(n)]
        for color, edges in [[red, redEdges], [blue, blueEdges]]:
            for start, end in edges:
            
                    color[start].add(end)

        d = [[float('inf')] * 2 for _ in range(n)]
        d[0] = [0, 0]
        que = deque([[0, 0], [0, 1]])

        while que:
            node, color = que.popleft()
            
            if color:
                edges = red
            else:
                edges = blue

            for neighbor in edges[node]:
                anti_color = 0 if color else 1
                if d[node][color] + 1 < d[neighbor][anti_color]:
                    d[neighbor][anti_color] = d[node][color] + 1
                    que.append([neighbor, anti_color])
        
        return [min(e) if min(e) < float('inf') else -1 for e in d]
