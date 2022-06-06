# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        return self.count(root, False)
    
    def count(self, node, is_left):
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return node.val if is_left else 0
        
        result = self.count(node.left, True)
        result += self.count(node.right, False)
        return result
