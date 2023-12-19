class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        res = 1
        left = 0
        nums.sort()
        cost = 0
        median = 0
        for right in range(1, len(nums)):
            right = max(left, right)
            cost += nums[right] - nums[median]
            median = (left + right + 1) // 2
            while cost > k:
                cost -= nums[median] - nums[left]    
                left += 1
                median = (left + right + 1) // 2
            res = max(res, right - left + 1)
        return res
