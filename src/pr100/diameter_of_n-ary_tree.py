"""
[3,null,1,null,5]
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        return self.rec(root)[1]

    def rec(self, node):
        if len(node.children) == 0:
            return 0, 0
        
        result = 0
        paths= []
        for child in node.children:
            len_path, sub = self.rec(child)
            result = max(result, sub)
            paths.append(len_path+1)
            paths.sort(reverse=True)
            if len(paths) > 2:
                paths = paths[:2]
        
        return paths[0], max(result, sum(paths))
        
