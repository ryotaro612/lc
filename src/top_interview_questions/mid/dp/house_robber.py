"""
n = len(nums)
memo = [-float('inf')]
memo[i] the best amount of money aquired by robbing houses[0..i] without alerm
memo[i] = max nums[i] + nums[i-2] or nums[i-1]
dp[i] = [money by robbing house of i, money by robbing houses but not house of i ]
dp[i+1][2] = [dp[i][1] + nums[i], max(dp[i][0], dp[i][1])]

[1,2]
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [nums[0], 0]
        for i in range(1, n):
            dp = [dp[1] + nums[i], max(dp[0], dp[1])]
        return max(dp)
