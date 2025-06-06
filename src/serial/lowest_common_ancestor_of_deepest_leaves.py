
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.rec(root)[1]

    def rec(self, node):
        if node is None:
            return 0, None
        
        left = self.rec(node.left)
        right = self.rec(node.right)

        if left[0] < right[0]:
            return right[0] + 1, right[1]
        elif left[0] > right[0]:
            return left[0]+1, left[1]
        
        return left[0]+1, node
