import bisect

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        lb = -1
        ub = nums[-1] - nums[0] + 1
        
        while ub - lb > 1:
            mid = (ub + lb) // 2
            temp = 0
            for left, num in enumerate(nums):
                right = bisect.bisect_right(nums, num+mid, left+1)
                temp += right - left - 1
            
            if k <= temp:
                ub = mid
            else:
                lb = mid
        return ub
