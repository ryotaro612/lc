# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.collect(root, result)
        return result
        
    def collect(self, node, acc) -> int:
        if node is None:
            return 0
        dist = max(self.collect(node.left, acc), self.collect(node.right, acc))
        if len(acc) <= dist:
            acc.append([])
        acc[dist].append(node.val)
        return dist + 1
