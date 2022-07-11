class Node:
    
    def __init__(self, prev, nxt, freq, words):
        self.prev = prev
        self.next = nxt
        self.freq = freq
        self.words = words
        
    def pop(self, key):
        self.words.remove(key)
    
    def isEmpty(self):
        return len(self.words) == 0
    
    def add_key(self, key):
        self.words.add(key)
    
    def get_one(self):
        return next(iter(self.words))
    
class AllOne:

    def __init__(self):
        self.head = None
        self.tail = None
        self.word_node = dict()

    def inc(self, key: str) -> None:
        if self.head is None:
            node = Node(None, None, 1, {key})
            self.head = node
            self.tail = node
            self.word_node[key] = node
        elif key in self.word_node:
            node = self.word_node[key]
            node.pop(key)
            next_freq = node.freq + 1
            if node.next is None:
                self.tail = Node(node, None, next_freq, {key})
                node.next = self.tail
            elif node.next.freq == next_freq:
                node.next.add_key(key)
            else:
                node.next.prev = Node(node, node.next, next_freq, {key})
                node.next = node.next.prev
        
            self.word_node[key] = node.next
            self.shrink(node)
        else:
            if self.head.freq == 1:
                self.head.add_key(key)
                self.word_node[key] = self.head
            else:
                node = Node(None, self.head, 1, {key})
                self.head.prev = node
                self.head = node
            self.word_node[key] = self.head
            
    def shrink(self, node):
        if node.isEmpty():
            if node.prev is None:
                self.head = node.next
            else:
                node.prev.next = node.next
            if node.next is None:
                self.tail = node.prev
            else:
                node.next.prev = node.prev    

    def dec(self, key: str) -> None:
        node = self.word_node[key]
        node.pop(key)
        next_freq = node.freq - 1
        
        if next_freq == 0:
            del self.word_node[key]
        else:
            if node.prev is None:
                self.head = Node(None, node, next_freq, {key})
                node.prev = self.head
            elif node.prev.freq == next_freq:
                node.prev.add_key(key)
            else:
                node.prev.next = Node(node.prev, node, next_freq, {key})
                node.prev = node.prev.next
                
            self.word_node[key] = node.prev
        self.shrink(node)

    def getMaxKey(self) -> str:
        if self.head is None:
            return ''
        else:
            return self.tail.get_one()

    def getMinKey(self) -> str:
        if self.head is None:
            return ''
        else:
            return self.head.get_one()


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
