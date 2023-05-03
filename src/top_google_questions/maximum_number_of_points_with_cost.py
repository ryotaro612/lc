class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        prev, dp = list(points[0]), list(points[0])
        n_row = len(points)
        n_col = len(points[0])
        for i in range(1, n_row):
            dp = []
            temp = -float("inf")
            for j in range(n_col):
                temp = max(temp, prev[j] + j)
                dp.append(temp - j + points[i][j])
            temp = -float("inf")
            for j in range(n_col - 1, -1, -1):
                temp = max(temp, prev[j] - j)
                dp[j] = max(dp[j], temp + j + points[i][j])
            prev = dp

        return max(dp)
