"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        return self.countDepth(root, 1)
    
    def countDepth(self, node, offset):
        if not node.children:
            return offset
        
        result = 0
        for child in node.children:
            result = max(result, self.countDepth(child, offset+1))
        return result
