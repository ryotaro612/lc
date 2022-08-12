"""
nodes = dict()
nodes[0] = [3, 15]
nodes[-1] = [9]
nodes[1]
nodes[2] = 

O(n+nlog(n) + n) >> (n + nlog(n))
O(n)



[3,1,4,0,2,2]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = collections.defaultdict(list)
        self.collect(root, 0, 0, nodes)
        
        result = [None] * len(nodes)
        offset = -min(nodes.keys())
        
        for col in nodes:
            result[col + offset] = [v for _, v in sorted(nodes[col])]
        return result
        
    def collect(self, node, row, col, nodes):
        if node is None:
            return
        
        nodes[col].append((row, node.val))
        
        self.collect(node.left, row+1, col - 1, nodes)
        self.collect(node.right, row+1, col + 1, nodes)
    
