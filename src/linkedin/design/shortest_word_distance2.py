
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        word_pos = defaultdict(list)
        for i, word in enumerate(wordsDict):
            word_pos[word].append(i)
        self.word_pos = word_pos
        
    def shortest(self, word1: str, word2: str) -> int:
        result = float('inf')
        i = 0
        n = len(self.word_pos[word1])
            
        for pos2 in self.word_pos[word2]:
            while i < n - 1 and self.word_pos[word1][i+1] < pos2:
                i += 1
            result = min(result, abs(pos2 - self.word_pos[word1][i]))
            if i < n - 1:
                result = min(result, abs(self.word_pos[word1][i+1] - pos2))
               
        return result


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
