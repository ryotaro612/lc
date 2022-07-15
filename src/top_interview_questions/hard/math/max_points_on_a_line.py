"""
[[0,0],[2,2],[-1,-1]]
"""
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n =len(points)
        if n == 1:
            return 1
        
        result = 0 
        
        for i in range(n-1):
            lines = defaultdict(set)

            for j in range(i + 1, n):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                
                a = y1 - y2
                b = x2 - x1
                c = -x2 * y1 + x1 * y1 + x1 * y2 - x1*y1
                key = self.normalize(a, b, c)
                for indice in [i, j]:
                    lines[key].add(indice)
               # print(lines)
            for nodes in lines.values():
                result = max(result, len(nodes))
        return result
    
    def normalize(self, a, b, c):
        if a < 0:
            a, b, c = -a, -b, -c
        if a > 0:
            g = math.gcd(math.gcd(a, b), c)
            a, b, c = a // g, b // g, c // g
            return (a, b, c)
        else: # a == 0
            if b < 0:
                b, c = -b, -c
            g = math.gcd(b, c)
            b, c = b // g, c // g
            return (a, b, c)
