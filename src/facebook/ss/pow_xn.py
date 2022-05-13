"""
n = 10 -> 1010
res = 1

res *= pow(2(x), pow(2, 2)) * pow(2(x), pow(2, 4))

n = 3 -> 11
res *= 1
res *= pow(2.1(x), pow(2, 1)) * pow(2.1(x), pow(2, 2))
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_negative = n < 0
        res = 1.0
        n = abs(n)
        while n > 0:
            if n & 1 > 0:
                if is_negative:
                    res *= 1.0 / x
                else:
                    res *= x
            n >>= 1
            x *= x
            
        return res
        
