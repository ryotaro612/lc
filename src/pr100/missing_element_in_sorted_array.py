
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ub, lb = n, -1

        while ub - lb > 1:
            mid = (ub + lb) // 2
            num_missing = nums[mid] - nums[0] - mid
            if k <= num_missing:
                ub = mid
            else:
                lb = mid
        return nums[0] + k + lb
        """
        nums[pos] <= missing val < nums[pos+1]
        pos is in [0, n] # n == len(nums)

        ub, lb 
        mid
        nums[mid] - nums[0] - 1 - (mid - 1) # num of missing val between nums[0] and nums[mid]
        == nums[mid] - nums[0] - mid
        is num_missing
        k < nummissing
        ub = mid
        """
