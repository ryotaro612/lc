class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.que = [0] * k
        self.left = 0
        self.right = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.size += 1
        self.left = self._backward(self.left)
        self.que[self.left] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.size += 1
        self.que[self.right] = value
        self.right = self._forward(self.right)
        return True    

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.left = self._forward(self.left)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.right = self._backward(self.right)
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[self.left]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.que[(self.right+self.k-1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.k == self.size

    def _forward(self, p):
        return (p + self.k + 1) % self.k
    
    def _backward(self, p):
        return (p + self.k - 1) % self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
