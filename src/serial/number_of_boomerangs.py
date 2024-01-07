from collections import defaultdict
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        """
        n
        n * (n-1) // 2
        """
        n = len(points)
        for i in range(n):
            dist_points = defaultdict(int)
            for j in range(n):
                if i == j:
                    continue
                x, y = points[i]
                x2, y2 = points[j]
                dist_points[(x2-x)**2 + (y2-y)**2] += 1
            
            for v in dist_points.values():
                result += v * (v-1)
        
        return result
