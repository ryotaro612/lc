import math
"""
[[2,1],[2,2],[3,3]]
90
[1,1]


[[2, 1],[1,2],[0,1],[1,0]]
0
[1, 1]

[[2,1],[2,2],[3,4],[1,1]]
90
[1,1]

[[1,0],[2,1]]
13
[1,1]

[[60,61],[58,47],[17,26],[87,97],[63,63],[26,50],[70,21],[3,89],[51,24],[55,14],[6,51],[64,21],[66,33],[54,35],[87,38],[30,0],[37,92],[92,12],[60,73],[75,98],[1,11],[88,24],[82,92]]
44
[15,50]
"""
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        base = 0
        temp = []
        for point in points:
            if point != location:
                temp.append(self.convertDegree(point[0] - location[0], point[1] - location[1]))
            else:
                base += 1
        
        n = len(temp)
        temp = sorted(temp)
        degrees = list(temp)
        for degree in temp:
            degrees.append(degree + 360)
        
        result = base
        end = 0
        for start in range(n):
            end = max(end, start)
            while angle - (degrees[end] - degrees[start]) >= -0.0001:
                end += 1
                result = max(result, base + end - start) 
            
        return result
        
        
    
    def convertDegree(self, x, y):
        
        r = math.sqrt(x * x + y * y)
        cos = x / r
        rad = math.acos(cos)
        
        if y < 0:
            rad = math.pi * 2 - rad
            
        return math.degrees(rad)
