# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.count(root, root.val)

    def count(self, node, threshold):
        if node is None:
            return 0
        result = 0
        if node.val >= threshold:
            result += 1

        next_threshold = max(node.val, threshold)

        return (
            result
            + self.count(node.left, next_threshold)
            + self.count(node.right, next_threshold)
        )
