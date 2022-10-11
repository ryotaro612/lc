from collections import defaultdict

class Node:
    
    def __init__(self, val):
        self.val = val
        self.children = dict()
        
class MapSum:

    def __init__(self):
        self.map = defaultdict(int)
        self.trie = Node(0)

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map[key]
        self.map[key] = val
        node = self.trie
        node.val += delta
        for c in key:
            if c in node.children:
                node = node.children[c]
                node.val += delta
            else:
                node.children[c] = Node(delta)
                node = node.children[c]
            
            

    def sum(self, prefix: str) -> int:
        node = self.trie
        n = len(prefix)
        for i, key in enumerate(prefix):
            if key in node.children:
                node = node.children[key]
            else:
                return 0
        return node.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
