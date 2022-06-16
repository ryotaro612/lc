# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
table = dict()
table[(None, None, 4)] = (Node(val=4), 1)
table[(Node(val=4), None, 2)] = Node(val=2)
"""
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        dups = dict()
        
        self.search(root, dups)
        result = []
        for node, freq in dups.values():
            if freq > 1:
                result.append(node)
        return result
    
    def search(self, node, dups):
        if node is None:
            return None
        
        represent_key = (self.search(node.left, dups), self.search(node.right, dups), node.val)
        if represent_key in dups:
            t = dups[represent_key]
            dups[represent_key] = (t[0], t[1] + 1) 
            return dups[represent_key][0]
        else:
            dups[represent_key] = (node, 1)
            return node
