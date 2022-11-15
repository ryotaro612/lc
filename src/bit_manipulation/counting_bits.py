"""
result = [..]
i 
result[i] = result[i - 2**x] + 1
result[5] = result[5 - 2**x] + 1
i - 1 < 2**x <= i
0   0
1   01
2   10
3   11
4  100
5  101 *
6  110
7  111
8 1000
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)
        x = 0
        for i in range(1, n+1):
            if i == 2**(x+1):
                x += 1
            
            result[i] = result[i-2**x] + 1
        
        return result
