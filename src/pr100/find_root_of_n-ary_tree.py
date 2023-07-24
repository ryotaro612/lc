"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
from collections import deque
class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        vals = {t.val: True for t in tree}
        for node in tree:
            for child in node.children:
                vals[child.val] = False
        
        v = [k for k in vals if vals[k]][0]
        return [t for t in tree if v == t.val][0]
