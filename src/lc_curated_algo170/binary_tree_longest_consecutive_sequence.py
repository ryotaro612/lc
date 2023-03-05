"""
[1,2,3,4,5]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        return self.rec(root, 0, 0)
    
    def rec(self, node, acc: int, best: int) -> int:
        result = 0
        for child in [node.left, node.right]:
            if child is None:
                result = max(result, acc+1, best)
            elif child.val == node.val + 1:
                result = max(result, self.rec(child, acc+1, max(best, acc+1)))   
            else:
                result = max(result, acc+1)
                result = max(result, self.rec(child, 0, best))
        return max(best, result)
