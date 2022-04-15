class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_row =len(matrix)
        n_col = len(matrix[0])
        
        r = n_row -1
        c = 0
        
        while 0 <= r and c < n_col:
            if matrix[r][c] == target:
                return True
            if 0 < r:
                if target <= matrix[r-1][c]:
                    r -= 1
                else:
                    c += 1
            else:
                c += 1
        return False
