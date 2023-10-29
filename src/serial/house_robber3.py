# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        result = self.traverse(root)
        return max(result)

    def traverse(self, node):
        if node is None:
            return [0] * 2
        
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        return [
                    max(left) + max(right),
            node.val + left[0] + right[0],
    
        ]
