class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        
        res = p0 = p1 = 0
        for c in text:
            if c == pattern[1]:
                res += p0
                p1 += 1
        
            if c == pattern[0]:
                p0 += 1

        return res + max(p0, p1)
