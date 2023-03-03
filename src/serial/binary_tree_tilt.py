# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        return self.compute_tilt(root)[0]

    def compute_tilt(self, node):
        if node is None:
            return 0, 0

        left_tilt, left_sum = self.compute_tilt(node.left)
        right_tilt, right_sum = self.compute_tilt(node.right)

        return left_tilt + right_tilt + abs(left_sum - right_sum), node.val + left_sum + right_sum
