# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        freq = [0] * 10
        return self.rec(root, freq)

    def rec(self, node, acc):
        """
        acc
        """
        if node.left is None and node.right is None:
            acc[node.val] += 1
            num_odd = 0
            for i in range(1, 10):
                if acc[i] % 2:
                    num_odd += 1
            acc[node.val] -= 1
            if num_odd > 1:
                return 0
            else:
                return 1

        acc[node.val] += 1
        result = 0
        for child in [node.left, node.right]:
            if child:
                result += self.rec(child, acc)
        acc[node.val] -= 1
        return result
