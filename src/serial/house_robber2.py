"""
[1]
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev = [-float('inf'), nums[0]]
        prev = self.calc(prev, nums)
        result = prev[0]
        prev = [0, -float('inf')]
        prev = self.calc(prev, nums)
        result = max(result, prev[0], prev[1])
        return result
    
    def calc(self, prev, nums):
        n = len(nums)
        for i in range(1, n):
            dp = [0] * 2
            dp[0] = max(prev)
            dp[1] = nums[i] + prev[0]
            prev = dp
        return prev
        
