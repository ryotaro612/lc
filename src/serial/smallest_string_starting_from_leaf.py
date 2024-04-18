# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
[4,0,1,1]
[25,1,null,0,0,1,null,null,null,0]

"""
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        cands = []
        self.rec(root, cands, [])
        result = min(cands)
        return ''.join([chr(ord('a') + v) for v in result])
    
    def rec(self, node, cands, tail):
        if node is None:
            return
        
        tail.append(node.val)

        if node.left and not node.right:
            self.rec(node.left, cands, tail)
        elif not node.left and node.right:
            self.rec(node.right, cands, tail)
        elif node.left and node.right:
            for child in [node.left, node.right]:
                self.rec(child, cands, tail)
        else:
            cands.append(list(tail)[::-1])
        tail.pop()
