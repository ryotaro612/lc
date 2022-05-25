class Solution:
    def validPalindrome(self, s: str) -> bool:
        result, [start, end] = self.isPalindrome(s, 0, len(s) - 1)
        if result:
            return True
        result, _ = self.isPalindrome(s, start+1, end)
        if result:
            return True
        return self.isPalindrome(s, start, end-1)[0]
    
    def isPalindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False, (start, end)
            else:
                start += 1
                end  -= 1
        return True, [start, end]
