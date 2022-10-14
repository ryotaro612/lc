class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        result = []
        cache = dict()
        for word in words:
            if len(word) == 1:
                continue
            for i in range(1, len(word)):
                if self.isConcat(word[:i], cache, word_set) and self.isConcat(word[i:], cache, word_set):
                    result.append(word)
                    break
        return result
    
    # word is concatenated one or more other words
    def isConcat(self, word, cache, word_set):
        if word in cache:
            return cache[word]
        if word in word_set:
            cache[word] = True
            return cache[word]
        
        for i in range(1,len(word)):
            if word[:i] in word_set:
                if self.isConcat(word[i:], cache, word_set):
                    cache[word] = True
                    return True
        cache[word] = False
        return False
