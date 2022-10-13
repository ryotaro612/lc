"""
[-1,0,3,5,9,12]
13
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = - 1
        ub = len(nums)
        while ub - lb > 1:
            mid = (ub + lb) // 2
            
            if nums[mid] >= target:
                ub = mid
            else:
                lb = mid
        
        if ub < len(nums) and -1 < ub and nums[ub] == target:
            return ub
        else:
            return -1
