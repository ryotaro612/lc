# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        result = []
        ok = self.traverse(root, voyage[::-1], result)
        return result if ok else [-1]
    
    def traverse(self, node, voyage, result):
        if node is None:
            return True
        
        if node.val != voyage[-1]:
            return False
        
        voyage.pop()
        if node.left and node.right:
            if voyage[-1] != node.left.val:
                result.append(node.val)
                node.left, node.right = node.right, node.left
        
        return self.traverse(node.left, voyage, result) and self.traverse(node.right, voyage, result)
