class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0
        for c in s:
            if c == 'A':
                a += 1
        if a > 1:
            return False
        
        for i in range(2, len(s)):
            if {s[i], s[i-1], s[i-2]} == {'L'}:
                return False

        return True
