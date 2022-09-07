class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        left_sum = 0
        n = len(nums)
        for i in range(n):
            if left_sum == total - nums[i] - left_sum:
                return i
            left_sum += nums[i]
        return -1
