# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
[10,5,15,3,7,null,18]
7
15
"""
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        return self.count(root, low, high)
    
    def count(self, node, low, high):
        if not node:
            return 0
        
        result = 0
        if low <= node.val <= high:
            result += node.val
        
        if low < node.val:
            result += self.count(node.left, low, high)
        if node.val < high:
            result += self.count(node.right, low, high)
            
        return result
