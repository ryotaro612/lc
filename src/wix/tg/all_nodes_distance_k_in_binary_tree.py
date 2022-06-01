# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        childToParent = dict()
        
        self.associate(root, None, childToParent)
        result = set()
        visited = set()
        self.search(target, visited, result, k, childToParent)
        return list(result)
    
    def associate(self, node, parent, childToParent):
        if node is None:
            return
        childToParent[node] = parent
        self.associate(node.left, node, childToParent)
        self.associate(node.right, node, childToParent)
        
    def search(self, node, visited, result, k, childToParent):
        if node is None or node.val in visited:
            return
        visited.add(node.val)
        if k == 0:
            result.add(node.val)
            return
        
        for neighbor in [childToParent[node], node.left, node.right]:
            self.search(neighbor, visited, result, k-1, childToParent)
