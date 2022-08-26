class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # O(n_row * n_col)
        #
        # dp[i][j] = dp[i][j-1] + dp[i-1][j]
        n_row = len(obstacleGrid)
        n_col = len(obstacleGrid[0])
        dp = [[0] * n_col for _ in range(2)]
        for i in range(n_col):
            if obstacleGrid[0][i]:
                break
            else:
                dp[0][i] = 1
        
        for i in range(1, n_row):
            for j in range(n_col):
                if obstacleGrid[i][j]:
                    dp[1][j] = 0
                elif j == 0:
                    dp[1][0] = dp[0][0]
                else:
                    dp[1][j] = dp[1][j-1] + dp[0][j]
            dp[0], dp[1] = dp[1], [0] * n_col
        
        return dp[0][-1]
