"""
0 .. n
0 5 10 15 20 .. 
O(nlog n)
n! min(num_of(2), num_of(5))

0 .. n

5 25 125 5^4 .. <= n

n // 5 + n // 25 + n // 125 + .. 
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        v = 5
        while v <= n:
            result += n // v
            v *= 5
        return result
