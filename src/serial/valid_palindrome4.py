class Solution:
    def makePalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        count = 0
        while left < right:
            if s[left] != s[right]:
                count +=1
            left += 1
            right -= 1
        return count < 3
        
