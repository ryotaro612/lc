import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        return self.rec(root)[0]

    def rec(self, node):
        if node is None:
            return 0, 0
        
        cost = 0
        delta = node.val - 1
        for child in [node.left, node.right]:
            c_cost, c_delta = self.rec(child)    
            cost += c_cost + abs(c_delta)
            delta += c_delta
        return cost, delta

