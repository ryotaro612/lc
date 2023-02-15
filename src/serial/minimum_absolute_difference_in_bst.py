# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        order = []
        self.rec(root, order)
        result = float('inf')
        for i in range(len(order) - 1):
            result = min(result, order[i+1] - order[i])
        return result
    
    def rec(self, node, order):
        if node is None:
            return
        self.rec(node.left, order)
        order.append(node.val)
        self.rec(node.right, order)
