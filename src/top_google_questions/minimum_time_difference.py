class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_points = []
        for point in timePoints:
            min_points.append(int(point[:2]) * 60 + int(point[3:5]))
        min_points.sort()
        min_points += [point + 60* 24 for point in min_points]

        result = float('inf')
        for i in range(len(min_points)-1):
            result = min(result, min_points[i+1] - min_points[i])
        return result
