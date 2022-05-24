# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lb, ub = 0, n
        
        while ub - lb > 1:
            mid = (ub + lb) // 2
            if isBadVersion(mid):
                ub = mid
            else:
                lb = mid
        return ub
