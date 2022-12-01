"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

[3,5,1,6,2,0,8,null,null,7,4]
5
1

[3,5,1,6,2,0,8,null,null,7,4]
5
4
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        ascend_p = set()
        node = p
        while node:
            ascend_p.add(node.val)
            node = node.parent
        
        node = q
        while node:
            if node.val in ascend_p:
                return node
            else:
                node = node.parent
        
