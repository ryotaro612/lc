class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        dp = [0, 1, 1]
        
        for i in range(3, n+1):
            temp = dp[2] + dp[1] + dp[0]
            dp[2], dp[1], dp[0] = temp, dp[2], dp[1]
            
        return dp[2]
