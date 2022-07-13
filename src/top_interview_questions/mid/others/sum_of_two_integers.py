"""
1 2 4 8 16 32 64 128 256 512 1024
0 1 2 3 4  5  6   7   8  9    10

-1000
-1000

0
0

-3
6
"""
class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a >= 0:
            if b >= 0:
                return self.bit_sum(a, b)
            else: # b < 0
                if abs(a) <= abs(b):
                    return -self.bit_sum(-a, -b)
                else:
                    return self.bit_sum(a, b)
        else: # a < 0
            if b >= 0:
                if abs(a) <= abs(b):
                    return self.bit_sum(a, b)
                else:
                    return -self.bit_sum(-a, -b)
            else: # b < 0
                return -self.bit_sum(-a, -b)
        
    def bit_sum(self, a, b):
        """a + b >= 0"""
        carry = 0
        result = 0
        for i in range(11):
            if a & (1 << i):
                if b & (1 << i):
                    if carry:
                        result |= 1 << i
                    else:
                        carry = 1
                else:
                    if carry:
                        pass
                    else:
                        result |= 1 << i
            else:
                if b & (1 << i):# 0 1
                    if carry: # 0 1 1
                        pass
                    else: # 0 1 0
                        result |= 1 << i
                else: # 0 0
                    if carry:
                        carry = 0
                        result |= 1 << i
                    else:
                        pass
        # print(result, bin(result), 0x11111111111 & result)
        return 0b11111111111 & result
                        
