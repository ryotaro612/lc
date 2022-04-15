# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
[6,2,8,0,4,7,9,null,null,3,5]
3
5
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is p or root is q:
            return root
        
        if p.val < root.val:
            if q.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return root
        else: # root.val < p.val
            if root.val < q.val:
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root
