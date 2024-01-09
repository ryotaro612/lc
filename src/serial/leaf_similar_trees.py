# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves = []
        self.collect_leaves(root1, leaves)
        leaves2 = []
        self.collect_leaves(root2, leaves2)
        return leaves == leaves2
    
    def collect_leaves(self, node, leaves):
        if node is None:
            return
        if node.left is None and node.right is None:
            leaves.append(node.val)
            return
        
        for child in [node.left, node.right]:
            self.collect_leaves(child, leaves)
        
        
