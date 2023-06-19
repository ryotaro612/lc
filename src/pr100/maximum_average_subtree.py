# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        return self.find_max(root)[0]

    def find_max(self, node):
        if node is None:
            return [0, 0, 0]

        left = self.find_max(node.left)
        right = self.find_max(node.right)

        total = left[1] + right[1] + node.val
        num = left[2] + right[2] + 1
        result = max([left[0], right[0], total / num])
        return [result, total, num]
