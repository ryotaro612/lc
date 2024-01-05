from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        dp = [[defaultdict(int) for _ in range(3)] for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][1][diff] += 1
                if diff in dp[j][1]:
                    dp[i][2][diff] += dp[j][1][diff]
                if diff in dp[j][2]:
                    dp[i][2][diff] += dp[j][2][diff]
            res += sum(dp[i][2].values())
        return res
