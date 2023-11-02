# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)[2]

    def traverse(self, node):
        if node is None:
            return [0, 0, 0]

        result = [node.val, 1, 0]
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        for i in range(3):
            result[i] += left[i] + right[i]
        
        if result[0] // result[1] == node.val:
            result[2] += 1
        
        return result
