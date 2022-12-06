class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        n = len(nums)
        right = 0
        window = 0
        result = float('inf')
        for left in range(n):
            right = max(left, right)
            
            while right < n and window < target:
                window += nums[right]
                right += 1
            if target <= window:
                result = min(result, right - left)
            
            window -= nums[left]
        
        return result
        
