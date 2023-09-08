# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.find(root, [], 0, result, targetSum)
        return result
    
    def find(self, node, path, sum_vals, result, targetSum):
        if node is None:
            return
        if node.left is None and node.right is None:
            if sum_vals + node.val == targetSum:
                result.append(list(path) + [node.val])
            return
        
        path.append(node.val)
        for child in [node.left, node.right]:
            self.find(child, path, sum_vals + node.val, result, targetSum)
        path.pop()
