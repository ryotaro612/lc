# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node_sum = []
        self.compute_sum(node_sum, root, 0)
        root.val = 0
        self.assign(root, 0, node_sum)
        return root

    def assign(self, node, depth, node_sum):
        total = 0

        for child in [node.left, node.right]:
            if child:
                total += child.val
            
        for child in [node.left, node.right]:
            if child:
                child.val = node_sum[depth+1] - total
                self.assign(child, depth+1, node_sum)

    
    def compute_sum(self, node_sum, node, depth):
        if node is None:
            return
        if len(node_sum) == depth:
            node_sum.append(node.val)
        else:
            node_sum[depth] += node.val

        for child in [node.left, node.right]:
            self.compute_sum(node_sum, child, depth+1)
