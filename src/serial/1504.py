class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
        8000000
        dp[r][c] = # of 1 continuous 1 from rc horizonal
        [0, 2] = 1
        [1, 2] = 0
        [1, 0] = 2
        dp[r][c] = dp[r][c+1]
        result = 0

        r, c
        result += dp[r][c]
        horizon = dp[r][c]
        horizon= min(dp[r][c], dp[r+][c])
        result += horizion * (r+i - r) 0<=i<=n_rows - r
        """
        result = 0
        n_rows = len(mat)
        n_cols = len(mat[0])
        dp = [[0] * n_cols for _ in range(n_rows)]

        for r in range(n_rows):
            for c in range(n_cols-1, -1, -1):
                if c == n_cols - 1:
                    if mat[r][c]:
                        dp[r][c] = 1
                    continue
                if mat[r][c]:
                    dp[r][c] = 1 + dp[r][c+1]
        # print(dp)
        result = 0
        for r in range(n_rows):
            for c in range(n_cols):
                h = dp[r][c]
                v = r
                while v < n_rows:
                    h = min(h, dp[v][c])
                    result += h

                    v += 1
        
        return result
