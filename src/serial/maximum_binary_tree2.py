# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.put(root, val)
    
    def put(self, node, val):
        if node is None:
            return TreeNode(val)
        
        if node.val < val:
            return TreeNode(val, node, None)        

        # node.val > val
        node.right = self.put(node.right, val)
        return node
