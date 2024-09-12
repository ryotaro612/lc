class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        lb = -1
        ub = 100000000
        while ub - lb > 1:
            mid = (ub + lb)// 2
            if mid * (mid+1) // 2 < target:
                lb = mid
            else:
                ub = mid
        
        while True:

            total = ub * (ub + 1) // 2

            if (total - target) % 2 == 0:
                return ub
            ub += 1
