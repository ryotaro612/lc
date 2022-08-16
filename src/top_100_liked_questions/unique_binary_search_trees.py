class Solution:
    def numTrees(self, n: int) -> int:
        dp = [-1] * (n+1)
        return self.rec(n, dp)
    
    def rec(self, n, dp):
        if dp[n] >= 0:
            return dp[n]
        elif n == 0:
            dp[n] = 1
            return dp[n]
        
        result = 0
        # use i[0, n-1]th node as root
        for i in range(n):
            n_left = self.rec(i, dp)
            n_right = self.rec(n-1-i, dp)
            result += n_left * n_right
        dp[n] = result
        return dp[n]
        
