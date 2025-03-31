# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = []
        self.collect(root, nodes)
        nodes = sorted(nodes)

        return self.make(nodes)

    def make(self, nodes):
        if not nodes:
            return
        
        n = len(nodes)

        mid = n // 2
        
        tree_node = TreeNode(nodes[mid])

        tree_node.left = self.make(nodes[:mid])
        if mid < n - 1:
            tree_node.right = self.make(nodes[mid+1:])
        
        return tree_node
    
    def collect(self, node, nodes):
        if node is None:
            return
        
        nodes.append(node.val)
        for child in [node.left, node.right]:
            self.collect(child, nodes)
