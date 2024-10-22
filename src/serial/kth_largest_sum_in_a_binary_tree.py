from collections import Counter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        ary = []
        self.rec(ary, root, 0)

        ary = sorted(ary, reverse=True)
        if len(ary) < k:
            return -1
        return ary[k-1]
    
    def rec(self, ary, node, depth):
        if node is None:
            return

        if len(ary) == depth:
            ary.append(node.val)
        else:
            ary[depth] += node.val

        for child in [node.left, node.right]:
            self.rec(ary, child, depth+1)
