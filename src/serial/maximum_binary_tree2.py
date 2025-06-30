# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ary = self.restore(root) + [val]
        return self.construct(ary)

    def construct(self, ary):
        if len(ary) == 0:
            return None

        maxi = max(ary)
        n = len(ary)
        for i in range(n):
            if maxi == ary[i]:
                left = self.construct(ary[:i])
                right = self.construct(ary[i+1:])
                return TreeNode(maxi, left, right)


    def restore(self, node):
        if node is None:
            return []

        return self.restore(node.left) + [node.val] + self.restore(node.right)
