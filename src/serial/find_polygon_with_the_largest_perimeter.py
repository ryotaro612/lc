class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        total = sum(nums)
        nums.sort()
        n = len(nums)
        for i in range(n-1,-1,-1):
            if nums[i] < total - nums[i] and i > 1:
                return total
            total -= nums[i]
        return -1
