
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = 0
        letters = dict()
        found = False
        for i, c in enumerate(s):
            if c in letters:
                result = max(result, i - letters[c] - 1)
                found = True
            else:
                letters[c] = i
        return result if found else -1
