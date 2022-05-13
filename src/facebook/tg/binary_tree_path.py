# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self._find_paths(root, [], res)
        return res
    
    def _find_paths(self, node, path, res):
        path.append(str(node.val))
        if node.left is None and node.right is None:
            res.append("->".join(path))
            path.pop()
            return 
        
        if node.left is not None:
            self._find_paths(node.left, path, res)
        if node.right is not None:
            self._find_paths(node.right, path, res)
        path.pop()
        return
