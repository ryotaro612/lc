class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set( "zxcvbnm")]
        result = []
        for word in words:
            for row in rows:
                if len([c for c in word.lower() if c in row]) == len(word):
                    result.append(word)
                    break
        return result
