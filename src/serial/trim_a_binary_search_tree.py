# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        """
        node.val < low
        -> rec(node.right)
        node.val > hight
        -> rec(node.left)
        low <= node.val <

        """
        return self.rec(root, low, high)

    def rec(self, node, low , high):
        if node is None:
            return
        if node.val < low:
            return self.rec(node.right, low, high)
        elif high < node.val:
            return self.rec(node.left, low, high)
        else:
            node.left =self.rec(node.left, low, high)
            node.right = self.rec(node.right, low, high)
            return node
