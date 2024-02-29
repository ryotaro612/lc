# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        return self.rec(root, 0)[1]

    def rec(self, node, depth):
        if node is None:
            return None
        
        result = [depth, node.val]
        for child in [node.left, node.right]:
            sub = self.rec(child, depth+1)
            if sub is not None and result[0] < sub[0]:
                result = sub
        return result
                
