"""
[5,2,9,8,4]
[[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]

[9,20,6,4,11,12]
[[0,3],[5,3],[2,4],[1,3]]

[16,14,9,16,25,22]
[[1,0],[0,2],[2,3],[4,3]]

[2,1,8,2,6,8]
[[0,4],[0,5],[1,4],[4,3],[1,2],[1,0],[2,3]]
"""
import heapq

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        g = [[] for _ in range(n)]
        for edge in edges:
            heapq.heappush(g[edge[0]], (-scores[edge[1]], edge[1]))
            heapq.heappush(g[edge[1]], (-scores[edge[0]], edge[0]))
 
        
        result = -1
        
        for node_a, node_b in edges:
            for node_x, node_y in [(node_a, node_b), (node_b, node_a)]:
                # print(node_a, node_b)
                node_c = self.findNode(g, node_x, {node_a, node_b})
                if node_c is not None:
                    node_d = self.findNode(g, node_y, {node_a, node_b, node_c})
                    if node_d is not None:
                        # print( [node_a, node_b, node_c, node_d])
                        # print(g)
                        result = max(result, sum([scores[i] for i in [node_a, node_b, node_c, node_d]]))
        
        return result
    
    
    def findNode(self, g, node, selected):    
        backup = []
        while g[node] and g[node][0][1] in selected:
            backup.append(heapq.heappop(g[node]))
        result = None
        if g[node]:
            result = g[node][0][1]
        while backup:
            heapq.heappush(g[node], backup.pop())
        
        # print(result, node, selected)
        return result
