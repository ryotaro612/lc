class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        peak, valley = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                peak = valley + 1
            elif nums[i] < nums[i-1]:
                valley = peak + 1
        return max(peak, valley)
