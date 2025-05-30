from collections import deque
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        dist1 = self.measure(node1, edges)
        dist2 = self.measure(node2, edges)

        n = len(edges)
        result = -1
        dist = float('inf')
        print(dist1, dist2)
        for i in range(n-1, -1, -1):
            if dist1[i] != float('inf') and dist2[i] != float('inf'):
                if dist >= max(dist1[i], dist2[i]):
                    dist = max(dist1[i], dist2[i])
                    result = i

        return result

    
    def measure(self, node, edges):
        n = len(edges)
        result = [float('inf')] * n
        result[node] = 0 
        que = deque([node])

        while que:
            i = que.popleft()
            if edges[i] == -1:
                continue
            
            if result[edges[i]] > result[i] + 1:
                result[edges[i]] = result[i] + 1
                que.append(edges[i])
        
        return result
    
