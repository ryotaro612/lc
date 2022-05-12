class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev = 1
        prev2 = 0
        current = 0
        
        for i in range(n):
            num = int(s[i])
            if 0 < num:
                current += prev
                #dp[i+1] += dp[i]
            if 0 < i and s[i-1] != '0':
                num = int(s[i-1:i+1])
                if 1 <= num and num <= 26:
                    current += prev2
                    # dp[i+1] += dp[i-1]
            prev2 = prev
            prev = current
            current = 0
        return prev    
        # return dp[n]
                                
