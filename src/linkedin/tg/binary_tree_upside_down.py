# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        result = self.rec(root)
        root.left = None
        root.right = None
        return result
    def rec(self, node):
        if node.left is None:
            return node
    
        new_root = self.rec(node.left)
        node.left.right = node
        node.left.left = node.right
        return new_root    
