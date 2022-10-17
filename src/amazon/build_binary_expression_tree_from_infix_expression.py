# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
"1-2+3+5-2-1-4"
"3*4-2*5"
"1-2+3-4"
"1-2*3*4+3*2*5-9*2*3*6"

"1-2+3"
"2-3/(5*2)+1"
"2-3/(5*2)"

"""
class Solution:
    def expTree(self, s: str) -> 'Node':
        stack = []
        depth = 0
        
        for c in s:            
            if c.isdigit():
                stack.append((Node(c), depth))
            
            elif c in {'+', '-'}:
                self.consumeMd(stack, depth)
                node = stack.pop()[0]
                if stack and stack[-1][1] == depth:
                    t = stack.pop()[0]
                    t.right = node
                    node = t
                stack.append((Node(c, node), depth))
                    
            elif c in {'*', '/'}:
                node = stack.pop()[0]
                if stack and stack[-1][1] == depth:
                    if stack[-1][0].val in {'+', '-'}:
                        stack.append((Node(c, node), depth))
                    elif stack[-1][0].val in {'*', '/'}:
                        prev = stack.pop()[0]
                        prev.right = node
                        stack.append((Node(c, prev), depth))
                    else:
                        assert False
                else:
                    stack.append((Node(c, node), depth))
            elif c == '(':
                depth += 1
            
            elif c == ')':
                node = stack.pop()[0]
                while stack and stack[-1][1] == depth:
                    parent, _ = stack.pop()
                    parent.right = node
                    node = parent
                depth -= 1                    
                stack.append((node, depth))
            #print(c)
            #print([self.debug(e[0]) for e in stack])
            #print('---')
        
        while len(stack) > 1:
            node = stack.pop()[0]
            stack[-1][0].right = node
        
        return stack[-1][0]
    
    
    def debug(self, node):
        if node is None:
            return ''
        elif node.val.isdigit():
            return node.val
        
        return f"({node.val}, {self.debug(node.left)}, {self.debug(node.right)})"
    
    def consumeMd(self, stack, depth):
        if stack and stack[-1][1] == depth:
            node = stack.pop()[0]
            if stack and stack[-1][1] == depth and stack[-1][0].val in {'*', '/'}:
                parent = stack.pop()[0]
                parent.right = node
                stack.append((parent, depth))
            else:
                stack.append((node, depth))
    
    def consume(self, stack, depth):
        if stack and stack[-1][1] == depth:
            node = stack.pop()[0]
            self.consumeMd(stack, depth)
            if stack and stack[-1][1] == depth:
                parent = stack.pop()[0]
                parent.right = node
                stack.append((parent, depth))
            else:
                stack.append((node, depth))
        node = stack.pop()[0]
        
    

            
