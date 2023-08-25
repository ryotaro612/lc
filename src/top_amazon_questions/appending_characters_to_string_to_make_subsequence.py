class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        i = 0
        n = len(t)
        for c in s:
            if i < n and c == t[i]:
                i += 1

        return max(0, n - i) 
