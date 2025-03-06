
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        bit = [0] * (n+1)

        res = 0
        mx = -1
        for pos in flips:
            pos = pos - 1
            self.add(bit, pos, 1)

            mx = max(mx, pos)
            if self.sum(bit, mx+1) == mx + 1:
                res += 1
        
        return res
        
    def add(self, bit, i, v):
        i += 1
        n = len(bit)
        while i < n:
            bit[i] += v
            i += i & (-i)
    
    def sum(self, bit, i):
        res = 0
        while i:
            res += bit[i]
            i -= i & (-i)
        
        return res


