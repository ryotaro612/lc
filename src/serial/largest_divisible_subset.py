from collections import defaultdict

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[1, i] for i in range(n)]
        max_i, max_v = 0, 1
        res_i = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i][0] < dp[j][0] + 1:
                    dp[i] = [dp[j][0]+1, j]
                    if dp[res_i][0] < dp[i][0]:
                        res_i = i
        
        result_size = dp[res_i][0]
        result = []
        # print(dp, result_size, res_i)
        while len(result) < result_size:
            result.append(nums[res_i])
            res_i = dp[res_i][1]
        return result

