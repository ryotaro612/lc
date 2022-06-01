# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    
        return self.search(root)[2]
    
    def search(self, node):
        if node is None:
            return [None, None, None]
        
        small, large = node.val, node.val
        result = 100000000
        [l_small, l_large, l_diff] = self.search(node.left)
        if l_small is not None:
            result = min(result, l_diff)
            small = l_small
            result = min(result, abs(node.val - l_large))
            
        [r_small, r_large, r_diff] = self.search(node.right)
        if r_large is not None:
            result = min(result, r_diff)
            large = r_large
            result = min(result, abs(node.val - r_small))
        return [small, large, result]
