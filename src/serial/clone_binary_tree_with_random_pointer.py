# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':

        copied = self.deepCopy(root)
        resolver = dict()
        self.assoc(root, copied, resolver)

        self.attachRandom(root, copied, resolver)
        return copied

    def deepCopy(self, node):
        if node is None:
            return None
        
        new_node = NodeCopy(node.val)
        new_node.left = self.deepCopy(node.left)
        new_node.right = self.deepCopy(node.right)
        return new_node
    
    def assoc(self, origin, copy, resolver):
        if origin is None:
            return
        resolver[origin] = copy

        self.assoc(origin.left, copy.left, resolver)
        self.assoc(origin.right, copy.right, resolver)

    def attachRandom(self, origin, copy, resolver):
        if origin is None:
            return

        copy.random = resolver.get(origin.random, None)
        self.attachRandom(origin.left, copy.left, resolver)
        self.attachRandom(origin.right, copy.right, resolver)
