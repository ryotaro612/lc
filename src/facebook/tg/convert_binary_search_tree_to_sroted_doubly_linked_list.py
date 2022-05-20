"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        left, right = self.connect(root)
        right.right = left
        left.left = right
        return left

    def connect(self, node):
        if node is None:
            return None, None
        
        left, right = self.connect(node.left)
        left2, right2 = self.connect(node.right)
        
        if left is None:
            if left2 is None:
                return node, node
            else:
                node.right = left2
                left2.left = node
                return node, right2
        else:
            if left2 is None:
                node.left = right
                right.right = node
                return left, node
            else:
                node.left = right
                right.right = node
                node.right = left2
                left2.left = node
                return left, right2
