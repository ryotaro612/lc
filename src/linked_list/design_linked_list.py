"""
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[0],[0]]
"""
class Node:
    
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        node = self._getNode(index)
        return node.val

    def addAtHead(self, val: int) -> None:
        self.size += 1
        self.head = Node(val, self.head)

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
        else:
            tail = self._getNode(self.size-1)
            tail.next = Node(val, None)
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            self.size += 1
            prev = self._getNode(index-1)
            prev.next = Node(val, prev.next)
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        elif index == self.size - 1:
            prev = self._getNode(self.size-2)
            prev.next = None
        else:
            prev = self._getNode(index-1)
            prev.next = prev.next.next
        self.size -= 1
        
    def _getNode(self, index) -> Node:
        node = self.head
        for _ in range(index):
            node = node.next
        return node

# 1 -> 3
# 1 -> 2 -> 3
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
