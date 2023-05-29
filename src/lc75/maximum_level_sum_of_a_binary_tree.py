# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sum_arr = []
        self.add(root, 0, sum_arr)

        mx = max(sum_arr)
        for i, s in enumerate(sum_arr):
            if s == mx:
                return i + 1

    def add(self, node, depth, sum_arr):
        if node is None:
            return
        if len(sum_arr) == depth:
            sum_arr.append(0)
        sum_arr[depth] += node.val

        for child in [node.left, node.right]:
            self.add(child, depth + 1, sum_arr)
