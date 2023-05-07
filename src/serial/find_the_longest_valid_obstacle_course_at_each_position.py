import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        dp, result = [float("inf")] * n, [0] * n

        for i, obstacle in enumerate(obstacles):
            indice = bisect.bisect_right(dp, obstacle)
            result[i] = indice + 1
            dp[indice] = obstacle
        return result
