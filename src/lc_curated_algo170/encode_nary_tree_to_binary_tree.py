"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if root is None:
            return None
        
        result = TreeNode(root.val)
        if not root.children:
            return result
        
        node_trees = [self.encode(child) for child in root.children]
        
        result.left = node_trees[0]
        node = node_trees[0]
        for child in node_trees[1:]:
            node.right = child
            node = child
        # print(result)
        return result
        
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        # print(data)
        if not data:
            return None
        result = Node(data.val, [])
        
        if data.left is None:
            return result
        
        result.children = [self.decode(data.left)]
        child = data.left
        while child.right:
            child = child.right
            result.children.append(self.decode(child))
        # print(data, '->', result)
        return result
    
    def debug(self, node):
        """
        print(node.val)
        for c in node.children:
            print(self.debug())
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))

"""
   1
  /
  3
 /  \
5    2
 \    \
  6    4
 
 
"""
