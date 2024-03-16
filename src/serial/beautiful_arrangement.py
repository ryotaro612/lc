from functools import cache
class Solution:
    def countArrangement(self, n: int) -> int:
    
        return self.rec(0, n, (1<<n) - 1)
    
    @cache
    def rec(self, left, right, mask):
        """
        n = 4
        """
        if left == right:
            return 1
        
        result = 0
        for i in range(right):
            if mask & (1<<i):
                if (left + 1) % (i+1) ==0 or (i+1) % (left + 1) == 0:
                    result += self.rec(left + 1, right, mask & ~(1<<i))
        return result
