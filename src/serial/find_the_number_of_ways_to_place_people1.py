class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        """
        2500
        125000
        (x1, y1), (x2, y2)
        """
        result = 0
        n = len(points)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if self.check(i, j, points):
                    
                    result += 1
        
        return result
    
    def check(self, i, j, points):
        n = len(points)
        x1, y1 = points[i]
        x2, y2 = points[j]

        if x1 <= x2 and y1 >= y2:
            for k in range(n):
                if k in {i, j}:
                    continue
                        
                x, y = points[k]
                if x1 <= x <= x2 and y2 <= y <= y1:
                    return False
        
            return True
