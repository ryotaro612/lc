class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        m = len(part)
        start = 0
 
        while True:
            for i in range(start, len(s)-m+1):
                if s[i:i+m] == part:
                    s = s[:i] + s[i+m:]
                    start = max(i-m, 0)
                    break
            else:
                return s

    
