
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return None
        
        result = []
        stack = []
        stack.append(root)
        
        while len(stack):
            node = stack.pop()
            result.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        return result            
