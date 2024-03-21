# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        """
        self.rec(root, 0)
        return root

    def rec(self, node, parent_sum):
        if node is None:
            return parent_sum

        result = 0
        right = self.rec(node.right, parent_sum)
        node.val += right
        left = self.rec(node.left, node.val)
        return left
