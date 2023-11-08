"""
1 2 1 2 1
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx, sy) == (fx, fy) and t == 1:
            return False
        if abs(sx-fx) <= abs(sy-fy):
            diff_x = abs(sx-fx)
            return t >= diff_x + (abs(sy-fy) - diff_x)
        else:
            diff_y = abs(sy-fy)
            return t >= diff_y + (abs(sx-fx) - diff_y)
