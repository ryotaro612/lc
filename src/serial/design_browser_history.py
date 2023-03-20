"""
[3,2,4,null,null,1]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.is_subtree(root)[4]

    def is_subtree(self, node):
        if node is None:
            return True, 0, float('inf'), -float('inf'), 0

        l_ok, l_num, l_lb, l_ub, l_res = self.is_subtree(node.left)
        r_ok, r_num, r_lb, r_ub, r_res = self.is_subtree(node.right)
        num = l_num + r_num + 1
        ok = l_ok and r_ok and l_ub < node.val < r_lb
        if ok:
            res = 1 + l_num + r_num
        else:
            res = max(l_res, r_res)
        return ok, num, min(l_lb, node.val), max(r_ub, node.val), res
