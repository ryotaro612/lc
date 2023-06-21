# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int
    ) -> bool:
        vals = set()
        self.collect(root1, vals)
        return self.find_pair(root2, vals, target)

    def find_pair(self, node, vals, target):
        if node is None:
            return False
        if target - node.val in vals:
            return True

        found = False
        for child in [node.left, node.right]:
            found = found or self.find_pair(child, vals, target)
        return found

    def collect(self, node, vals):
        if node is None:
            return
        vals.add(node.val)
        for child in [node.left, node.right]:
            self.collect(child, vals)
