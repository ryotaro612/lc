class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        
        res = self.lastRemaining(n//2)
        if n % 2:
            return n-1 - 2 * (res-1)
        else:
            return n - 2 * (res-1)
