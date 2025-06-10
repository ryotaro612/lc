class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = 0
        n = len(nums)
        result = 0
        for left in range(n):
            right = max(right, left)
            while right < n and nums[left] + k >= nums[right] - k:
                right += 1
            
            
            result = max(result, right - left)
        
        return result
