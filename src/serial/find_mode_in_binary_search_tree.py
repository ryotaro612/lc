from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)

        self.count(root, counter)

        max_freq = max(counter.values())
        return [k for k in counter if counter[k] == max_freq]

    def count(self, node, counter):
        if node == None:
            return
        counter[node.val] += 1
        self.count(node.left, counter)
        self.count(node.right, counter)
