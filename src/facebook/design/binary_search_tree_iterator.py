# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.val =  - 1
        self.update = False
        
    def next(self) -> int:
        if self.update:
            self.update = False
            return self.val
        
        self.val = self._find_egt(self.root, self.val)
        return self.val

    def hasNext(self) -> bool:
        if self.update:
            return self.val is not None
    
        self.val = self._find_egt(self.root, self.val)
        self.update = True
        return self.val is not None
    
    def _find_egt(self, node, val):
        if node is None:
            return None

        if val < node.val:
            candidate = self._find_egt(node.left, val)
            if candidate is None:
                return node.val
            return candidate
        else: # node.val < val
            return self._find_egt(node.right, val)
            
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
