from collections import deque
class StringIterator:

    def __init__(self, compressedString: str):
        self.que = deque(compressedString)
        self.letter = None
        self.freq = None
        
    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.letter is None:
            self.letter = self.que.popleft()
            self.freq = 0
            while self.que and self.que[0].isdigit():
                self.freq *= 10
                self.freq += int(self.que.popleft())
        
        result = self.letter
        self.freq -= 1
        if not self.freq:
            self.letter = None
        
        return result

    def hasNext(self) -> bool:
        return self.letter or self.que


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
