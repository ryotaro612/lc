"""
"2251799813685247"
"""
import math
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        
        for count in range(int(math.log(n, 2))+1, 1, -1):
            lb, ub = 1, n
            while ub - lb > 1:
                mid = (ub+lb) // 2
                val = 0
                for i in range(count-1, -1, -1):
                    val += mid**i
                    if n < val:
                        break
                if n < val:
                    ub = mid
                elif n == val:
                    return str(mid)
                else:
                    lb = mid
        
