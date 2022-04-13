"""
[[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n_row = len(matrix)
        n_col = len(matrix[0])
        left = False
        top = False
        for i in range(0, n_row):
            if matrix[i][0] == 0:
                left = True
        for i in range(0, n_col):
            if matrix[0][i] == 0:
                top = True
                
                
        for i in range(1, n_row):
            for j in range(1, n_col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(1, n_row):
            if matrix[i][0] == 0:
                for j in range(1, n_col):
                    matrix[i][j] = 0
                    
        for i in range(n_col):
            if matrix[0][i] == 0:
                for j in range(1, n_row):
                    matrix[j][i] = 0

        if left:
            for i in range(n_row):
                matrix[i][0] = 0
        if top:
            for i in range(n_col):
                matrix[0][i] = 0  
        
