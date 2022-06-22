"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
None: "[]"
node is leaf => [node.val]
node has children => [node.val[..][..]] 

"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        
        if root is None:
            return "[]"
        result = f"[{root.val}" + ''.join([self.serialize(child) for child in root.children]) + "]"
        #print(result)
        return result
	
    def deserialize(self, data: str) -> 'Node':
        if data == '[]':
            return None
        
        i = data.find('[', 1)
        if i == -1:
            return Node(int(data[1:-1]), [])
        
        val = int(data[1:i])
        children = []
        stack = []
        for i in range(i, len(data) - 1):
            if data[i] == '[':
                stack.append(i)
            elif data[i] == ']':
                left = stack.pop()
                if len(stack) == 0:
                    children.append(self.deserialize(data[left:i+1]))
        print(data, val, [v.val for v in children])
        return Node(val, children)
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
