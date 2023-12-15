from collections import defaultdict
"""
[[0,0,1,1],[0,1,3,2],[1,0,2,2]]
"""
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        bl_x = float('inf')
        bl_y = float('inf')
        tr_x = -float('inf')
        tr_y = -float('inf')
        area_rectangles = 0
        points = defaultdict(int)
        
        for [x, y, a, b] in rectangles:
            bl_x = min(bl_x, x)
            bl_y = min(bl_y, y)
            tr_x = max(tr_x, a)
            tr_y = max(tr_y, b)
            area_rectangles += (a - x) * (b - y)
            
            for i in [x, a]:
                for j in [y, b]:
                    points[(i, j)] += 1
        odds = {k for k in points if points[k] % 2}

        return area_rectangles == (tr_y - bl_y) * (tr_x - bl_x) and odds == {(bl_x, bl_y), (bl_x, tr_y), (tr_x, tr_y), (tr_x, bl_y)}
        
