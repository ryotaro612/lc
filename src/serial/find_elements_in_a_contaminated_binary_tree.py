# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.found = set()

        self.rec(root, 0, self.found)

    def rec(self, node, value, found):
        if node is None:
            return
        
        found.add(value)
        self.rec(node.left, value*2+1, found)
        self.rec(node.right, value*2+2, found)        

    def find(self, target: int) -> bool:
        
        return target in self.found
