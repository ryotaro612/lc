class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n_row, n_col = len(mat), len(mat[0])

        if n_row * n_col != r * c:
            return mat

        result = [[None] * c for _ in range(r)]

        for i in range(n_row * n_col):
            result[i // c][i % c] = mat[i // n_col][i % n_col]
        return result
