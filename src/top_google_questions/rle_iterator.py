class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.i = 0
        self.encoding = encoding
        

    def next(self, n: int) -> int:

        while True:
            if self.i == len(self.encoding):
                return -1
            elif self.encoding[self.i] >= n:
                self.encoding[self.i] -= n
                return self.encoding[self.i+1]
            else:
                n -= self.encoding[self.i]
                self.i += 2
