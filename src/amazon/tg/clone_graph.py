"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        visited = dict()
        self.deepCopy(node, visited)
        return visited[node.val]
    
    def deepCopy(self, node: 'Node', visited):
        if node.val in visited:
            return
        
        n = Node(int(node.val))
        visited[node.val] = n
        for neighbor in node.neighbors:
            self.deepCopy(neighbor, visited)
        for neighbor in node.neighbors:
            n.neighbors.append(visited[neighbor.val])
