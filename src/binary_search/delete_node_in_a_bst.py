# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
[5,3,6,2,4,null,7]
3

[5,3,6,2,4,null,7]
0

[5,3,6,2,4,null,7]
3

[5,3,6,2,4,null,7]
7
[4,null,7,6,8,5,null,null,9]
7
"""
class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                if root.right is None:
                    return None
                else:
                    successor = self.findSuccessor(root)
                    root.val = successor.val
                    root.right = self.deleteNode(root.right, root.val)
            else:
                predecessor = self.findPredecessor(root)
                root.val = predecessor.val
                root.left = self.deleteNode(root.left, root.val)
        return root
        
    def findSuccessor(self, node):
        if node.right is None:
            return None
        node = node.right
        while node.left:
            node = node.left
        return node
    
    def findPredecessor(self, node):
        if node.left is None:
            return None
        node = node.left
        while node.right:
            node = node.right
        return node
