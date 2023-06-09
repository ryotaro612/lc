"""
[[5,6],[5,6],[5,6],[4,6]]
"""


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        n_row, n_col = len(mat), len(mat[0])
        index = [0] * n_row
        for e in mat[0]:
            for i in range(1, n_row):
                while index[i] < n_col and mat[i][index[i]] < e:
                    index[i] += 1

                if index[i] == n_col:
                    return -1
                if e < mat[i][index[i]]:
                    break
                if i == n_row - 1:
                    return e
        return -1
