# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        found = set()
        return self.traverse(root, found, k)
    
    def traverse(self, node, found, k):
        if node is None:
            return False
        
        if k - node.val in found:
            return True
        found.add(node.val)
        return any(self.traverse(child, found, k) for child in [node.left, node.right])
