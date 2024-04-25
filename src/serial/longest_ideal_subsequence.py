class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [-float('inf')] * 27
        dp[26] = 0
        for c in s:
            c_i = ord(c) - ord('a')
            next_dp = list(dp)
            for i in range(27):
                if i == 26:
                    next_dp[c_i] = max(next_dp[c_i], 1)
                else:
                    if abs(c_i - i) <= k:
                        next_dp[c_i] = max(next_dp[c_i], dp[i] + 1)
            dp = next_dp
        
        return max(dp)
