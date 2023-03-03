# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.is_same(root, subRoot):
            return True
        
        if root is None:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def is_same(self, node1, node2):
        if node1 is None:
            if node2:
                return False
            else:
                return True
        if node2 is None:
            return False

        if node1.val == node2.val:
            return self.is_same(node1.left, node2.left) and self.is_same(node1.right, node2.right)
        return False
