"""
p1 p2
p3 p4

[0,0]
[1,1]
[1,0]
[0,1]

[0,0]
[1,1]
[1,0]
[0,12]

[1,0]
[-1,0]
[0,1]
[0,-1]

[0,0]
[5,0]
[5,4]
[0,4]

[0,0]
[5,0]
[5,4]
[0,4]
"""
import itertools
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        for a, b, c, d in itertools.permutations([p1, p2, p3, p4]):
            """
            a b
            c d
            """
            if len({b[0] - a[0], b[1] - d[1], d[0] - c[0], a[1] - c[1]}) == 1 and \
                b[0] - a[0] > 0 and \
                self.is_right_angle(a, b, c) and \
                self.is_right_angle(b, a, d) and \
                self.is_right_angle(d, b, c) and \
                self.is_right_angle(c, a, d):
                # print(a, b, c, d,b[0] - a[0])
                return True
        return False

    def is_right_angle(self, a, b, c):
        e = [b[0] - a[0], b[1] - a[1]]
        f = [c[0] - a[0], c[1] - a[1]]
        return e[0] * f[0] + e[1] * f[1] == 0
