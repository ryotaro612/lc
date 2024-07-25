
import random
import bisect

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        remap = dict()
        bs = set(blacklist)
        n_b = len(blacklist)
        start = n - n_b
        for b in blacklist:
            if b <= n- 1 - n_b:
                while start in bs:
                    start += 1
                remap[b] = start
                start += 1

        self.remap = remap 
        self.n = n
        # print(self.remap)
        self.blacklist = blacklist
    def pick(self) -> int:
        i = random.randint(0, self.n-1-len(self.blacklist))
        if i not in self.remap:
            return i
        return self.remap[i]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
