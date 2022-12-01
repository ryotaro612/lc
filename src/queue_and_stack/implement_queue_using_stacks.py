class MyQueue:

    def __init__(self):
        self.stack = []
        self.reverse = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if self.reverse:
            return self.reverse.pop()
        else:
            self.reverse = self.stack[::-1]
            self.stack = []
            return self.pop()

    def peek(self) -> int:
        if self.reverse:
            return self.reverse[-1]
        else:
            return self.stack[0]
        

    def empty(self) -> bool:
        return self.stack == [] and self.reverse == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
