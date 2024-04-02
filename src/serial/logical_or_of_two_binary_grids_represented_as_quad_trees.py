"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            if quadTree1.val:
                return quadTree1
            else:
                return quadTree2
        if quadTree2.isLeaf:
            if quadTree2.val:
                return quadTree2
            else:
                return quadTree1
        
        node = Node(
            0,
            False,
            self.intersect(quadTree1.topLeft, quadTree2.topLeft),
            self.intersect(quadTree1.topRight, quadTree2.topRight),
            self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft),
            self.intersect(quadTree1.bottomRight, quadTree2.bottomRight),
        )
        if all([tree.isLeaf for tree in [node.topLeft, node.topRight, node.bottomLeft, node.bottomRight]]):
            if node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val:
                return Node(node.topLeft.val, True, None, None, None, None)
        return node
                    
            
