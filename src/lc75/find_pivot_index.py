class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        left = 0
        for i, num in enumerate(nums):
            if left == total - num - left:
                return i
            left += num
        return -1
