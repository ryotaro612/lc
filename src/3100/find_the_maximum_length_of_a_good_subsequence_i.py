class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[-float('inf')] * (k+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1

        result = 1
        for i in range(n):
            for j in range(i):
                for l in range(k+1):
                    if nums[i] == nums[j]:
                        dp[i][l] = max(dp[i][l], 1 + dp[j][l])
                        result = max(result, dp[i][l])
                    else:
                        if l < k:
                            dp[i][l+1] = max(dp[i][l+1], 1 + dp[j][l])
                            result = max(result, dp[i][l+1])

        return result
