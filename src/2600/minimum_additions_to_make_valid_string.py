class Solution:
    def addMinimum(self, word: str) -> int:
        prev = 'z'
        k = 0
        for c in word:
            k += c <= prev
            prev = c

        return k * 3 - len(word)   
