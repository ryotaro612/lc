class Solution(object):
    
    def cherryPickup(self, grid):
        n = len(grid)
        dp = [[[None] * n for _ in range(n)] for _ in range(n)]
        
        res =  self.solve(0, 0, 0, n, dp, grid)
        # print(dp)
        return max(0, res)
    def solve(self, r1, c1, r2, n, dp, grid):
        c2 = r1 + c1 - r2
        
        if self.is_outbound(r1, c1, n) or self.is_outbound(r2, c2, n):
            return float('-inf')

        if dp[r1][c1][r2] is not None:
            return dp[r1][c1][r2]
        
        if grid[r1][c1] == -1 or grid[r2][c2] == -1:
            dp[r1][c1][r2] = float('-inf')
            return dp[r1][c1][r2]
        
        if r1 == n - 1 and c1 == n - 1:
            dp[r1][c1][r2] = grid[r1][c1]
            return dp[r1][c1][r2]
    
        if r1 == r2:
            res = grid[r1][c1]
        else:
            res = grid[r1][c1] + grid[r2][c2]
        
        res += max(self.solve(r1+1, c1, r2+1, n, dp, grid), self.solve(r1+1, c1, r2, n, dp, grid), self.solve(r1, c1+1, r2+1, n, dp, grid), self.solve(r1, c1+1, r2, n, dp, grid))
        dp[r1][c1][r2] = res
        return res
    
    def is_outbound(self, r, c, n):
        return not (0 <= r and r < n and 0 <= c and c < n)
