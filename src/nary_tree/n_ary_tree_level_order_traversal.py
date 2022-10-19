"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        que = deque()
        
        if root is None:
            return []
    
        result = []
        que.append((root, 0))
        while que:
            node, level = que.popleft()
            
            if level < len(result):
                result[level].append(node.val)
            else:
                result.append([node.val])
            
            for child in node.children:
                que.append((child, level+1))
        
        return result
