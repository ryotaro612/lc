class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = [[0] * n for _ in range(n+1)]

        for i, num in enumerate(nums):
            for v in range(n):
                count[i+1][v] = count[i][v]
            count[i+1][num] += 1

        dp = [[float('inf')] * (n+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i, num in enumerate(nums):
            offset = dp[i][i]
            for j in range(i):
                if count[i+1][num] - count[j][num] == 2:
                    dp[i+1][j] = min(dp[i][j] + 2, dp[i+1][j])
                elif count[i+1][num] - count[j][num] > 2:
                    dp[i+1][j] = min(dp[i][j] + 1, dp[i+1][j])
                else:
                    dp[i+1][j] = min(dp[i][j], dp[i+1][j])
                offset = min(offset, dp[i][j])
            # dp[i+1][i] = min(k + min(dp[i][:i+1]), dp[i+1][i])
            dp[i+1][i] = min(k + offset, dp[i+1][i])
        """
        for row in dp:
            print(row)
        """
        return min(dp[n])
