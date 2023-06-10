class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lb = -1
        ub = maxSum * (n + 1)
        while ub - lb > 1:
            mid = (ub + lb) // 2
            # 0 1 2 3 4
            total = self.sumUp(mid, index + 1) + self.sumUp(mid - 1, n - index - 1)
            # print(mid, self.sumUp(mid, index+1), self.sumUp(mid-1, n-index-1))
            if total + n > maxSum:
                ub = mid
            else:
                lb = mid
        return lb + 1

    def sumUp(self, high, length):
        # high, high - 1, high - 2, ... max(0, high- (length-1))
        total = high * (high + 1) // 2
        if high <= length:
            return total

        total -= (high - length) * (high - length + 1) // 2
        return total
