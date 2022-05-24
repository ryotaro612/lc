"""
[5,0,0,0]
3
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dp = dict()
        n = len(nums)
        running_sum = 0
        dp[0] = -1
        for i in range(n):
            running_sum += nums[i]
            running_sum %= k
            
            if running_sum in dp:
                pos = dp[running_sum]
                if pos < i - 1:
                    return True
            else:
                dp[running_sum] = i
        return False
