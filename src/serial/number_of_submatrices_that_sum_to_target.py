from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n_rows, n_cols = len(matrix), len(matrix[0])
        prefix = [[0] * n_cols for _ in range(n_rows)]
        for r in range(n_rows):
            for c in range(n_cols):
                prefix[r][c] = matrix[r][c]
                if r:
                    prefix[r][c] += prefix[r-1][c]
                if c:
                    prefix[r][c] += prefix[r][c-1]
                if r and c:
                    prefix[r][c] -= prefix[r-1][c-1]
        res = 0
        # print(prefix)
        for c1 in range(n_cols):
            for c2 in range(c1, n_cols):
                mp = defaultdict(int)
                mp[0] = 1
                for r in range(n_rows):
                    acc = prefix[r][c2] - (prefix[r][c1-1] if c1 else 0)
                    res += mp[acc - target]
                    mp[acc] += 1

        return res
