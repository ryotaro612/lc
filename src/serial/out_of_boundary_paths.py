class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        prev = [[0] * n for _ in range(m)]
        res = 0
        mod = 10**9 + 7
        prev[startRow][startColumn] = 1
        for _ in range(maxMove):
            dp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    for n_r, n_c in [[r-1, c], [r, c+1], [r+1, c], [r, c-1]]:
                        if 0 <= n_r < m and 0 <= n_c < n:
                            dp[n_r][n_c] += prev[r][c]
                        else:
                            res += prev[r][c]
                            res %= mod
            prev = dp
        return res
