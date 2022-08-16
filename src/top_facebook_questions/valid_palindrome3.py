class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        n = len(s)
        dp = [0] * (n+1)
        for i in reversed(range(0, n)):
            for j in range(i+1, n+1):
                if i == j - 1:
                    prev = 0
                    dp[j] = 0
                else:
                    next_prev = dp[j]
                    # dp[j] -> dp[i+1][j]
                    # dp[j-1] -> dp[i][j-1]
                    if s[i] == s[j-1]:
                        dp[j] = prev
                    else:
                        dp[j] = min(prev+2, dp[j]+1, dp[j-1]+1)
                    prev = next_prev
            #print(i)
            #print(dp)
        """
        for i in range(n):
            for j in range(i+1, n+1):
                print(s[i:j], '->', dp[i][j])
        """
        #print(dp[n])
        return dp[n] <= k
