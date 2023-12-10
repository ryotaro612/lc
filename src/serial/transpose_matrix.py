class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # r, c -> c, r
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        result = [[0] * n_rows for _ in range(n_cols)]
        for r in range(n_rows):
            for c in range(n_cols):
                result[c][r] = matrix[r][c]
        return result
