"""
[1,6,7,5,4,null,null,null,null,3,null]
[24,25,25,26,24,26,24,25,27,23,23,25,25,23,23,26,24,26,28,24,22,22,24,26,26,26,26,22,24,22,22,null,27,null,25,null,25,null,27,null,25,null,21,null,23,23,23,null,25,null,25,null,27,27,25,null,23,null,23,null,21,21,21]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)[0]

    def traverse(self, node):
        inc = 1
        result = 1
        dec = 1
        for child in [c for c in [node.left, node.right] if c]:
            sub = self.traverse(child)
            result = max(result, sub[0])
            if child.val == node.val + 1:
                inc = max(inc, sub[1] + 1)
            if child.val == node.val - 1:
                dec = max(dec, sub[2] + 1)
        result = max(result, inc + dec - 1)
        return [result, inc, dec]
