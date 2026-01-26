# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        
        return self.count(root, [])
    
    def count(self, node, path):
        if node is None:
            return 0
        
        result = 0
        if len(path) > 1:
            if path[-2].val % 2 == 0:
                result += node.val
        
        path.append(node)
        for child in [node.left, node.right]:
            result += self.count(child, path)
        
        path.pop()
        return result
