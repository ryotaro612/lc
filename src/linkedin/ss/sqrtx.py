class Solution:
    def mySqrt(self, x: int) -> int:
        lb, ub = -1, x + 1
        
        while ub - lb > 1:
            mid = (ub + lb) // 2
            if x < mid ** 2:
                ub = mid
            else:
                lb = mid
        return lb
