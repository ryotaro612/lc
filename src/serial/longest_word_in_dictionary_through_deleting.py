class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = ''
        for word in dictionary:
            i = 0
            is_sub = False
            for c in s:
                if word[i] == c:
                    i += 1
                    if i == len(word):
                        is_sub = True
                        break
            if is_sub:
                if len(result) < len(word):
                    result = word
                elif len(result) == len(word):
                    result = min(result, word)
        return result
