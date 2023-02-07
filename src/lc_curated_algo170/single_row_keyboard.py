class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pos = 0
        res = 0
        c_p = {c:i for i, c in enumerate(keyboard)}
        for c in word:
            res += abs(c_p[c] - pos)
            pos = c_p[c]
        return res
