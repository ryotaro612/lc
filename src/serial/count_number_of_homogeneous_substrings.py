class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9 + 7
        result = 0
        streak = 0
        for i in range(len(s)):
            if i and s[i-1] == s[i]:
                streak += 1
            else:
                streak = 1

            result = (result + streak) % mod 
        return result
