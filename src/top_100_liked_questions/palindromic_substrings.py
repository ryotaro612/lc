
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n):
            result += self.count(s, i, i)
            result += self.count(s, i, i+1)
        
        return result

    def count(self, s, start, end):
        result = 0
        n = len(s)
        while 0<= start and end <= n-1:
            if s[start] == s[end]:
                result += 1
                start -= 1
                end += 1
            else:
                break
        return result    
