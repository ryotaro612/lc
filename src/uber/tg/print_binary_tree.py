# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.computeHeight(root, 0)
        m = height + 1
        n = 2**m - 1
        result = [[""] * n for _ in range(m)]
        
    def computeHeight(self, node, height):
        if node is None:
            return height
        
        return max(self.computeHeight(node.left, height+1), 
                   self.computeHeight(node.right, height+1))
