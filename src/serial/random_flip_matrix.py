import random

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.ones = set()

    def flip(self) -> List[int]:
        v = self.select(0, self.n * self.m)
        self.ones.add(v)
        return [v // self.n, v % self.n] 
    
    def reset(self) -> None:
        self.ones = set()

    def select(self, left, right) -> int:
        if left >= right:
            return -1
        # print(left, right-1)
        i = random.randint(left, right-1)
        if i not in self.ones:
            return i
        result = []
        result.append(self.select(left, i))
        result.append(self.select(i+1, right))
        result = [v for v in result if v >= 0]
        
        return result[random.randint(0, len(result)-1)] if result else -1

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
