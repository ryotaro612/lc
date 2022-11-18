class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n_row = len(matrix)
        n_col = len(matrix[0])
        dp = [0] * n_col
        for i in range(n_col):
            dp[i] = matrix[0][i]
            
        for r in range(1, n_row):
            next_dp = [float('inf')] * n_col
            for i in range(n_col):
                if 0 < i:
                    next_dp[i-1] = min(next_dp[i-1], dp[i] + matrix[r][i-1])
                next_dp[i] = min(next_dp[i], dp[i] + matrix[r][i])
                
                if i < n_col - 1:
                    next_dp[i+1] = min(next_dp[i+1], dp[i] + matrix[r][i+1])
            
            dp = next_dp
            
        return min(dp)
