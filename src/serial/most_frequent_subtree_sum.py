from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        self.count_subtree_sum(root, freq)
        max_freq = max(list(freq.values()))
        return [k for k in freq if freq[k] == max_freq]

    def count_subtree_sum(self, node, freq):
        if node is None:
            return 0
        val = node.val
        for child in [node.left, node.right]:
            val += self.count_subtree_sum(child, freq)
        freq[val] += 1
        return val
