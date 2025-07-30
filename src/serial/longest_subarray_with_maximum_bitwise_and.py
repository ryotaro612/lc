class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi = max(nums)
        result = 1
        left = right = 0
        n = len(nums)
        while left < n:
            if nums[left] != maxi:
                left += 1
                right = left
                continue
            while right < n and nums[right] == maxi:
                right += 1
            
            result = max(result, right - left)
            left = right
        return result
            
