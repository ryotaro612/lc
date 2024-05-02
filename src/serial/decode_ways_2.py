class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(1, n+1):
            d = ord(s[i-1]) - ord('0')
        
            if 0 <= d <= 9:
                if d:
                    dp[i] += dp[i-1]
    
                if i > 1:
                    d2 = ord(s[i-2]) - ord('0')
                    if 0 < d2 <= 2 and 10 <= d2 * 10 + d <= 26:
                        dp[i] += dp[i-2]
                    elif s[i-2] == '*':
                        for dec in [10, 20]:
                            if 10 <= dec + d <= 26:
                                dp[i] += dp[i-2]

            elif s[i-1] == '*':
                dp[i] += 9 * dp[i-1]

                if i > 1:
                    d2 = ord(s[i-2]) - ord('0')
                    if 0 < d2 <= 2:
                        for a in range(1, 10):
                            if 0 < d2 * 10 + a <= 26:
                                dp[i] += dp[i-2]
                    elif s[i-2] == '*':
                        # 11 .. 19 21..26
                        dp[i] += dp[i-2] * 15
        
            dp[i] %= 10**9 + 7
            
        return dp[n]
