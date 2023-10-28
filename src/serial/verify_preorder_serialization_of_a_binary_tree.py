class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        serial = [v != '#' for v in preorder.split(',')][::-1]
        return self.check(serial) and len(serial) == 0
    
    def check(self, nodes):
        if not nodes:
            return True
        if not nodes[-1]:
            nodes.pop()
            return True
        
        if len(nodes) < 3:
            return False
        nodes.pop()
        return self.check(nodes) and self.check(nodes)
