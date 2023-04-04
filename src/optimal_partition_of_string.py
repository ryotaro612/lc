class Solution:
    def partitionString(self, s: str) -> int:
        arr = list(s)
        letters = set()
        result = 0
        while arr:
            letter = arr.pop()
            if letter in letters:
                result += 1
                letters = {letter}
            else:
                letters.add(letter)
        return result + 1
