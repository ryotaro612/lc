class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        nums[2m] == nums[2m+1]
        0 <= m
        nums[2m-1] == nums[2m]
        """
        n = len(nums)
        lb, ub = -1, n

        while ub - lb > 1:
            mid = (ub + lb) // 2
            if 0 < mid:
                if mid < n - 1:
                    if nums[mid-1] != nums[mid] and nums[mid] != nums[mid+1]:
                        return nums[mid]
                else: # mid == n-1
                    if nums[mid-1] != nums[mid]:
                        return nums[mid]
            else:
                if mid < n-1:
                    if nums[mid] != nums[mid+1]:
                        return nums[mid]
                else:
                    return nums[0]
            
            if mid % 2:
                if nums[mid-1] == nums[mid]:
                    lb = mid
                else:
                    ub = mid
            else:
                if mid < n -1 and nums[mid] == nums[mid+1]:
                    lb = mid
                else:
                    ub = mid
        
