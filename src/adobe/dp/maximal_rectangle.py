"""
(0, 0)(1, 0)
n_row = len(matrix) # n_row
m_mu = len(matrix[0])
dp = [0 for _ in n]

        # if matrix[i][current_col-k] = 1
            matrix[i][current_col-k+1] = 1
            ..
            matrix[i][current_col] = 1
            dp[i]= k + 1
            
            matrix[i][j]
            dp[i]
            2 * min(dp[i], dp[i-1])
            3 * min(dp[i], dp[i-1], [i-2])
            ..
            n_row * n_col * n_row
            n_row
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n_row, n_col = len(matrix), len(matrix[0])
        dp = [0 for _ in range(n_row)]
        result = 0
        for j in range(n_col):
            for i in range(n_row):
                if int(matrix[i][j]) == 1:
                    dp[i] += 1
                else:
                    dp[i] = 0
            for i in range(n_row):
                result = max(result, dp[i])
                width = dp[i]
                k = i
                while k >= 0:
                    if dp[k] == 0:
                        break
                    width = min(width, dp[k])
                    result = max(width * (i - k + 1), result)
                    k -= 1
        return result
              
