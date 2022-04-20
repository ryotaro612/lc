class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        i = 0
        while i < n - 1 - i:
            if s[i] != s[n-1-i]:
                return False
            i += 1
        return True
