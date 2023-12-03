class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(1, len(points)):
            x, y = points[i-1]
            next_x, next_y = points[i]
            diff_x = abs(next_x - x)
            diff_y = abs(next_y - y)
            com = min(diff_x, diff_y)
            result += com + abs(diff_x - diff_y)
        return result
