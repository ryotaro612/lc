class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        words = set(dictionary)
        dp = [i for i in range(n+1)]
        for i in range(n+1):
            for j in range(i):
                if s[j:i] in words:
                    dp[i] = min(dp[i], dp[j])
                else:
                    dp[i] = min(dp[i], dp[j] + i - j)

        return dp[n]
