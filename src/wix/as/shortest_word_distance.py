class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d1, d2 = -1000000, 100000000
        result = abs(d1 - d2)
        
        for index, word in enumerate(wordsDict):
            if word == word1:
                d1 = index
            elif word == word2:
                d2 = index
            result = min(result, abs(d1 - d2))
        return result
