class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        result = 0
        for right in range(n):
            right = max(right, left)
            if right - left + 1 < 3:
                continue
            if nums[right] - nums[right-1] == nums[right-1] - nums[right-2]:
                result += right - 1 - left
            else:
                left = right - 1

        return result
