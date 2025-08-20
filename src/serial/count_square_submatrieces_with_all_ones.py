class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        dp[r][c] = 3

        dp[r][c] = 1 + min(dp[r+1][c+1], dp[r+1][c], dp[r][c+1])
        matrix[r][c] = 0 -> dp[r][c] = 0
        dp[r][c] = min
        
        result = 0
        result += dp[r][c]
        """
        n_row = len(matrix)
        n_col = len(matrix[0])

        result = 0
        dp = [[0] * n_col for _ in range(n_row)]
        for r in range(n_row-1, -1, -1):
            for c in range(n_col-1, -1, -1):
                if matrix[r][c] == 0:
                    continue
                
                if r < n_row - 1 and c < n_col - 1:
                    l = min(dp[r+1][c+1], dp[r+1][c], dp[r][c+1])
                else:
                    l = 0
                dp[r][c] = 1 + l
                result += dp[r][c]
        return result
