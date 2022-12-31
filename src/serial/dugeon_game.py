class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n_row = len(dungeon)
        n_col = len(dungeon[0])

        dp = [[float('inf')] * n_col for _ in range(n_row)]
        
        for i in range(n_row-1, -1, -1):
            for j in range(n_col -1 , -1, -1):
                if i == n_row - 1:
                    if j == n_col - 1:
                        dp[i][j] = 1 - dungeon[i][j]
                    else:
                        dp[i][j] = dp[i][j+1] - dungeon[i][j]
                else:
                    if j == n_col - 1:
                        dp[i][j] = dp[i+1][j] - dungeon[i][j]
                    else:
                        dp[i][j] = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(1, dp[i][j])
        print(dp)
        return dp[0][0]
