class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        """
        result = 0
        """
        left = right = 0
        prev_left = prev_right = -1
        result = 0
        n = len(nums)
        while right < n:
            while right < n - 1 and nums[right] < nums[right+1]:
                right += 1
                result = max(result, (right - left + 1)// 2)
            
            if prev_left != -1:
                result = max(result, min(prev_right - prev_left + 1, right - left + 1))
            
            prev_left = left
            prev_right = right
            left = right = right + 1
            
        return result
