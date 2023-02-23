# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        self.traverse(root, nodes)
        order = sorted([node.val for node in nodes])
        for i in range(len(nodes)):
            nodes[i].val = order[i]
        

    def traverse(self, node, order):
        if node is None:
            return
        
        self.traverse(node.left, order)
        order.append(node)
        self.traverse(node.right, order)

       
       
