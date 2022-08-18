# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
[1]
0

[10,5,-3,3,2,null,11,3,-2,null,1]
8
"""
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counts = defaultdict(int)
        return self.findPaths(root, counts, 0, 0, targetSum)
    
    
    def findPaths(self, node, counts, running_sum, acc, targetSum):
        if node is None:
            return acc
        
        running_sum += node.val
        
        if running_sum == targetSum:
            acc += 1
            
        
        acc += counts[running_sum-targetSum]
        counts[running_sum] += 1
        
        for child in [node.left, node.right]:
            acc = self.findPaths(child, counts, running_sum, acc, targetSum)
        
        counts[running_sum] -= 1
        return acc    
