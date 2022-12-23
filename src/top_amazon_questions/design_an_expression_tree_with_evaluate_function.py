import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


    def evaluate(self) -> int:
        if self.val in {'+', '-', '*', '/'}:
            left = self.left.evaluate()
            right = self.right.evaluate()
            if self.val == '+':
                return left + right
            elif self.val == '-':
                return left - right
            elif self.val == '*':
                return left * right
            elif self.val == '/':
                return left // right
        else:
            return int(self.val)
        

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        
        if postfix:
            val = postfix.pop()
            if val in {'+', '*', '-', '/'}:
                tree = Node(val)
                tree.right = self.buildTree(postfix)
                tree.left = self.buildTree(postfix)
                return tree
            else:
                return Node(val)
        else:
            return None

"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
