"""
[1]
[1,2]
"""
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        lb, ub = -1, len(nums)
        while ub - lb > 1:
            mid = (lb + ub) // 2
            if nums[mid] < nums[mid+1] if mid < n - 1 else -pow(2, 31) - 1:
                lb = mid
            else:
                ub = mid
        return min(ub, n-1)
