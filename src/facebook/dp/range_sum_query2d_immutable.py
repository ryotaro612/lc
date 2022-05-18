class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n_row = len(matrix)
        n_col = len(matrix[0])
        matrix_sum = [[0] * n_col for _ in range(n_row)]
        matrix_sum[0][0] = matrix[0][0]
        for i in range(1, n_col):
            matrix_sum[0][i] += matrix_sum[0][i-1] + matrix[0][i]
        for i in range(1, n_row):
            matrix_sum[i][0] += matrix_sum[i-1][0] + matrix[i][0]
        
        for i in range(1, n_row):
            for j in range(1, n_col):
                matrix_sum[i][j] += matrix[i][j]
                matrix_sum[i][j] += matrix_sum[i-1][j]
                matrix_sum[i][j] += matrix_sum[i][j-1]
                matrix_sum[i][j] -= matrix_sum[i-1][j-1]
        self.matrix_sum = matrix_sum
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        result = self.matrix_sum[row2][col2]
        if row1 > 0:
            result -= self.matrix_sum[row1-1][col2]
        if col1 > 0:
            result -= self.matrix_sum[row2][col1-1]
        if row1 > 0 and col1 > 0:
            result += self.matrix_sum[row1-1][col1-1]
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
