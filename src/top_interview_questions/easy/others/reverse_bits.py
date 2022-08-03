class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(0, 32):
            if n & (1 << i) > 0: # (0.. 31)
                result |= 1 << (31 - i)
            
        return result
