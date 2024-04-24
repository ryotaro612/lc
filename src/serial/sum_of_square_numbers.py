import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        b = int(math.sqrt(c))

        a = 0
        while a <= b:
            cand = a * a + b * b
            if cand == c:
                return True
            elif cand < c:
                a += 1
            else:
                b -= 1
        return False
