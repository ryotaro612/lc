"""
que = [0] * k
size = 0
front = index to append the next enqueued item

"""

class MyCircularQueue:

    def __init__(self, k: int):
        self.que = [0] * k
        self.size = 0
        self.front = 0

    def enQueue(self, value: int) -> bool:
        if self.size == len(self.que):
            return False
        self.que[self.front] = value
        self.front = (self.front + 1) % len(self.que)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        return True
        
    def Front(self) -> int:
        if self.size == 0:
            return -1
        
        return self.que[(self.front + len(self.que) - self.size) % len(self.que)]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.que[(self.front -1 + len(self.que)) % len(self.que)]
        
    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == len(self.que)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
