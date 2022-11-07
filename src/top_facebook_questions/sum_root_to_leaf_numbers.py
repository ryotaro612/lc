# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, 0)
    
    def traverse(self, node, prefix):
        if not (node.left or node.right):
            return prefix * 10 + node.val
        
        result = 0
        for child in [node.left, node.right]:
            if child:
                result += self.traverse(child, prefix * 10 + node.val)
        
        return result
