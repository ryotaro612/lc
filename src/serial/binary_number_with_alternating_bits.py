class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = n & 1
        n >>= 1
        while n:
            if bit == (n & 1):
                return False
            bit = n & 1
            n >>= 1
        return True
