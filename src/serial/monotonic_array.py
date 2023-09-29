class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return self.is_inc(nums) or self.is_dec(nums)

    def is_inc(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return False
        return True
    def is_dec(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                return False
        return True
