class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        na = len(a)
        nb =len(b)
        if na != nb:
            return max(na, nb)
        
        return na
