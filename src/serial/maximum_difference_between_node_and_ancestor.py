# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)[2]

    def traverse(self, node):
        if node.left is None and node.right is None:
            return node.val, node.val, 0
        
        mini = float('inf')
        maxi = -float('inf')
        res = 0
        for child in [node.left, node.right]:
            if child:
                c_min, c_max, c_res = self.traverse(child)
                res = max(c_res, res, abs(node.val - c_min), abs(node.val - c_max))
                mini = min(c_min, mini, node.val)
                maxi = max(c_max, maxi, node.val)
        return mini, maxi, res
