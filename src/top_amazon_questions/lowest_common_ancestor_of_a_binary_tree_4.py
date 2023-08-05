# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        return self.find(root, {node.val for node in nodes})[1]

    def find(self, node, vals):
        if node is None:
            return 0, None
        count = 0
        if node.val in vals:
            count += 1
        for child in [node.left, node.right]:
            sub_count, ancestor = self.find(child, vals)
            if ancestor:
                return sub_count, ancestor
            count += sub_count
        
        if count == len(vals):
            return count, node
        else:
            return count, None
        
