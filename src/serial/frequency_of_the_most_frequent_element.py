class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = nums[i] + prefix_sum[i]
        
        left = 0
        result = 0
        for right, num in enumerate(nums):
            while (right - left + 1) * num > (prefix_sum[right+1] - prefix_sum[left]) + k:
                left += 1
            result = max(result, right -left+1)

        return result
