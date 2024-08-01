class Solution:
    def longestWord(self, words: List[str]) -> str:
        result = ""
        words = sorted(words)

        seen = {""}
        for word in words:
            if word[:-1] in seen:
                if len(result) < len(word):
                    result = word
                elif len(result) == len(word):
                    if word < result:
                        result = word
                
                seen.add(word)
        return result

