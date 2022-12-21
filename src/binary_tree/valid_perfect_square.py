class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        ub = num + 1
        lb  = 0
        while ub - lb > 1:
            mid = (ub + lb) // 2
            
            if mid ** 2 <= num:
                lb = mid
            else:
                ub = mid
        return lb * lb == num
