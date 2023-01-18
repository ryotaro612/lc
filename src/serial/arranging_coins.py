class Solution:
    def arrangeCoins(self, n: int) -> int:
        ub = n + 1
        lb = 0
        while ub - lb > 1:
            mid = (ub + lb) // 2
            if n >= mid * (mid + 1) // 2:
                lb = mid
            else:
                ub = mid
        return ub - 1
