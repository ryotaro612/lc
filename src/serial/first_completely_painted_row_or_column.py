class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        v_cell = dict()
        n_rows = len(mat)
        n_cols = len(mat[0])
        for r in range(n_rows):
            for c in range(n_cols):
                v_cell[mat[r][c]] = [r, c]

        row_counter = [0] * n_rows
        col_counter = [0] * n_cols

        for i, e in enumerate(arr):
            r, c = v_cell[e]
            row_counter[r] += 1
            col_counter[c] += 1

            if row_counter[r] == n_cols or col_counter[c] == n_rows:
                return i
        

