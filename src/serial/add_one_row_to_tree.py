# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,root)

        self.append_rows(root, 1, val, depth)
        return root
    
    def append_rows(self, node, cur_depth, val, depth):
        if node is None:
            return
        
        if cur_depth < depth - 1:
            for child in [node.left, node.right]:
                self.append_rows(child, cur_depth+1, val, depth)
            return
        
        # cur_depth == depth - 1
        
        node.left = TreeNode(val, node.left)
        node.right = TreeNode(val, None, node.right)
