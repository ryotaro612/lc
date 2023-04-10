# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        result = cols
        for i in range(rows):
            ub, lb = cols, -1
            while ub - lb > 1:
                mid = (ub + lb) // 2

                if binaryMatrix.get(i, mid):
                    ub = mid
                else:
                    lb = mid
            result = min(ub, result)
        return -1 if result == cols else result
