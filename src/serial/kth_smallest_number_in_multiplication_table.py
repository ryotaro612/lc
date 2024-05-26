class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lb = 0
        ub = m*n + 1
        while ub - lb > 1:
            mid = (ub + lb) // 2

            count = 0
            for i in range(1, n+1):
                count += min(mid // i, m)
            
            if count < k:
                lb = mid
            else:
                ub = mid
            
        return ub
