class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n_rows, n_cols = len(mat), len(mat[0])
        row_freq = [0] * n_rows
        col_freq = [0] * n_cols
        for r in range(n_rows):
            for c in range(n_cols):
                if mat[r][c]:
                    row_freq[r] += 1
                    col_freq[c] += 1
        result = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if mat[r][c]:
                    if row_freq[r] == col_freq[c] == 1:
                        result += 1
        return result
