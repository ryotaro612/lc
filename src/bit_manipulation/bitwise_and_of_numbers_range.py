"""
result = left

result = 0b1001001
              *
         0b1001111 < 0b1010000 <= right
"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        result = left
        
        for i in range(32):
            if result & (1 << i):
                v = result | ((1 << i) - 1)
                if v < right:
                    result &= ((1 << 32) - 1) ^ (1 << i) 
        return result
