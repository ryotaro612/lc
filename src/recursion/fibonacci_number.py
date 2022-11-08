class Solution:
    def fib(self, n: int) -> int:
        dp = dict()
        
        return self.fib_dp(n, dp)
    
    def fib_dp(self, n, dp):
        if n in dp:
            return dp[n]
        if n == 0:
            dp[n] = 0
            return dp[n]
        elif n == 1:
            dp[n] = 1
            return dp[n]
        else:
            dp[n] = self.fib_dp(n-1, dp) + self.fib_dp(n-2, dp)
            return dp[n]
            
