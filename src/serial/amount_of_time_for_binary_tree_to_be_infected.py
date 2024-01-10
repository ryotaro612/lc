# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        child_parent = dict()
        self.associate(root, None, child_parent)
        start_node = self.find_start(root, start)

        return self.compute_distance(start_node, 0, None, child_parent)
    
    def associate(self, node, parent, child_parent):
        if node is None:
            return
        if parent is not None:
            child_parent[node.val] = parent

        for child in [node.left, node.right]:
            self.associate(child, node, child_parent)

    def find_start(self, node, start_val):
        if node is None:
            return None

        if node.val == start_val:
            return node
        
        for child in [node.left, node.right]:
            found = self.find_start(child, start_val)
            if found is not None:
                return found

    
    def compute_distance(self, node, depth, prev, child_parent):        
        
        res = depth
        for child in [node.left, node.right]:
            if child and child is not prev:
                res = max(res, self.compute_distance(child, depth+1, node, child_parent))
        
        if node.val in child_parent and prev is not child_parent[node.val]:
            res = max(res, self.compute_distance(child_parent[node.val], depth+1, node, child_parent))
        
        return res
