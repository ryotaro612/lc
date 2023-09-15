# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.visit(root, result, 0)
        return result[::-1]

    def visit(self, node, result, height):
        if node is None:
            return
        # print(node.val, height, result)
        if len(result) == height:
            result.append([])
        result[height].append(node.val)
        for child in [node.left, node.right]:
            self.visit(child, result, height+1)
