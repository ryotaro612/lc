# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
[3,9,20,null,null,15,7]
[1,2,2,3,3,null,null,4,4]
[1,2,3,4,5,6,null,8]
[3,9,20,null,null,15,7]
[1,null,2,null,3]
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        n = self.count(root)
        height, ok = self.measureHeight(root)
        height -= 1
        if not ok:
            return False
        
        print(height, n)
        #return 2 ** (maxHeight) <= n <= 2**(maxHeight+1)
        return n <= 2 ** (height + 2) - 1
    
    def measureHeight(self, node):
        if not node:
            return 0, True
        
        left_height, l_result = self.measureHeight(node.left)
        right_height, r_result = self.measureHeight(node.right)
        return 1 + max(left_height, right_height), abs(left_height - right_height) <= 1 and l_result and r_result
    
    
    def count(self, node):
        if node is None:
            return 0
        
        return 1 + self.count(node.left) + self.count(node.right)
