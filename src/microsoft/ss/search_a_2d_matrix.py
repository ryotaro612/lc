class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lb = -1
        ub = len(matrix)
        while 1 < ub - lb:
            mid = (ub + lb) // 2
            if target < matrix[mid][0]:
                ub = mid
            else:
                lb = mid
        
        row = lb
        lb = -1
        ub = len(matrix[0])
        while 1 < ub - lb:
            mid = (ub + lb) // 2
            if target < matrix[row][mid]:
                ub = mid
            else:
                lb = mid
        return target == matrix[row][lb]
