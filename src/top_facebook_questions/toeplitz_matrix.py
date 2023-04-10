class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n_row = len(matrix)
        n_col = len(matrix[0])
        for r, c in [(r, 0) for r in range(n_row-1, -1, -1)] + [(0, c) for c in range(n_col)]:
            while 0 <= r + 1 < n_row and 0 <= c + 1  < n_col:
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
                r +=1 
                c +=1
        return True
            
