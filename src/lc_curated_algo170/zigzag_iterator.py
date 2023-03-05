class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i = [0] * 2
        self.vv  = [v1, v2]
        self.p = 0

    def next(self) -> int:
        res = self.vv[self.p][self.i[self.p]]
        self.i[self.p] += 1
        self.p += 1
        self.p %= 2
        return res

    def hasNext(self) -> bool:
        if len(self.vv[self.p]) > self.i[self.p]:
            return True
        self.p += 1
        self.p %= 2
        return len(self.vv[self.p]) > self.i[self.p]
