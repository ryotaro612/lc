from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        result = 0
        freq = defaultdict(int)
        n = len(nums)
        right = 0
        for left in range(n):
            while right < n and freq[nums[right]] < k:
                freq[nums[right]] += 1 
                right += 1
                result = max(result, right - left)
            
            if left < right:
                freq[nums[left]] -= 1
        
        return result
