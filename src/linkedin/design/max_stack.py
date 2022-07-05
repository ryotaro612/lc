import heapq

class MaxStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        

    def push(self, x: int) -> None:
        idx = len(self.stack)
        self.stack.append((x, True))
        heapq.heappush(self.heap, (-x, -idx))        

    def pop(self) -> int:
        self._cleanStack()
        return self.stack.pop()[0]

    def top(self) -> int:
        self._cleanStack()
        # print('stack', self.stack, 'heap', self.heap)
        return self.stack[-1][0]
    
    def peekMax(self) -> int:
        self._cleanHeap()
        return -self.heap[0][0]

    def popMax(self) -> int:
        self._cleanHeap()
        x, idx = heapq.heappop(self.heap)
        self.stack[-idx] = (-x, False)
        return -x
    
    def _cleanStack(self):
        while self.stack[-1][1] == False:
            self.stack.pop()

    def _cleanHeap(self):
        while True:
            x, idx = self.heap[0]
            x, idx = -x, -idx
            if len(self.stack) <= idx or self.stack[idx][0] != x or self.stack[idx][1] == False:
                heapq.heappop(self.heap)
            else:
                return
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
