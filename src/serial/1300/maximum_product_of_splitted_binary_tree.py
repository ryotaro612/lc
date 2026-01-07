# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        
        total = self.compute_sum(root)
        mod = 10**9 + 7
        return self.find(root, total)[0] % mod
    
    def find(self, node, total):
        if node.left is None and node.right is None:
            return node.val * (total - node.val), node.val
        
        result = 0
        sub = node.val
        if node.left:
            result, l_total = self.find(node.left, total)
            sub += l_total
        if node.right:
            r_result, r_total = self.find(node.right, total)
            sub += r_total
            result = max(result, r_result)
        
        result = max(result, sub * (total - sub))
        return result, sub

    def compute_sum(self, node):
        if node is None:
            return 0
        result = node.val
        for child in [node.left, node.right]:
            result += self.compute_sum(child)
        
        return result
