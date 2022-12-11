# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
[1,null,2,3,4]
[1,2,3,4,5,6,null,null,null,7,8,9,10]
[1,2,3,null,4,5,null,6,7]
"""
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        left_boundaries = [] 
        if root.left:
            self.find_left_boundaries(root.left, left_boundaries)
        leaves = []
        self.find_leaves(root, root, leaves)
        right_boundaries = []
        if root.right:
            self.find_right_boundaries(root.right, right_boundaries)
        
        return [root.val] + left_boundaries + leaves + right_boundaries[::-1]
    
    def find_left_boundaries(self, node, boundaries):
        if node.left:
            boundaries.append(node.val)
            self.find_left_boundaries(node.left, boundaries)
        elif node.right:
            boundaries.append(node.val)
            self.find_left_boundaries(node.right, boundaries)
    
    def find_leaves(self, node, root, leaves):
        if node.left:
            self.find_leaves(node.left, root, leaves)
        if node.right:
            self.find_leaves(node.right, root, leaves)
        
        if node != root and node.left is None and node.right is None:
            leaves.append(node.val)
        
    def find_right_boundaries(self, node, boundaries):
        if node.right:
            boundaries.append(node.val)
            self.find_right_boundaries(node.right, boundaries)
        elif node.left:
            boundaries.append(node.val)
            self.find_right_boundaries(node.left, boundaries)
            
        
            
