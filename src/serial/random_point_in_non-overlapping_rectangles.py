import random
import bisect
from collections import defaultdict
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects        
        self.acc = list(accumulate([(x-a+1) * (y-b+1) for a,b, x,y in self.rects]))

    def pick(self) -> List[int]:
        idx = bisect.bisect_left(self.acc, random.randint(0, self.acc[-1]))
        rect = self.rects[idx]
        x = random.randint(rect[0], rect[2])
        y = random.randint(rect[1], rect[3])
        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
