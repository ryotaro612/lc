# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        (st, v)
        """
        sums = []
        self.acc(root, 0, sums)
        return [total/count for total, count in sums]

    def acc(self, node, depth, sums):
        if not node:
            return
        if len(sums) == depth:
            sums.append([node.val, 1])
        else:
            sums[depth] = [sums[depth][0] + node.val, sums[depth][1] + 1]
        
        for child in [node.left, node.right]:
            self.acc(child, depth+1, sums)
