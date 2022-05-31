class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        
        if n & (n-1) != 0:
            return False
        
        return n & 0x55555555 > 0
