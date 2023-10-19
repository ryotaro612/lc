# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = dict()
        result = self.build_tree(n, memo)
        return result

    def build_tree(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 1:
            memo[n] = [TreeNode(0)]
            return memo[n]
        if n < 1:
            return []
        # n > 1
        result = []
        n - 1
        for left in range(n):
            right = n - 1 - left
            left_trees = self.build_tree(left, memo)
            right_trees = self.build_tree(right, memo)
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(0, left_tree, right_tree)
                    result.append(root)
        memo[n] = result
        return memo[n]
