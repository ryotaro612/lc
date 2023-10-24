# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, 0, result)
        return result
    
    def traverse(self, node, height, result):
        if node is None:
            return
        
        if len(result) == height:
            result.append(node.val)
        else:
            result[height] = max(result[height], node.val)
        
        for child in [node.left, node.right]:
            self.traverse(child, height+1, result)
