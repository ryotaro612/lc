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
        if right is None:
            left = node
        else:
            right.right = node
            node.left = right
        
        left2, right2 = self.connect(node.right)
        if left2 is None:
            return left, node
        else:
            left2.left = node
            node.right = left2
            return left, right2
