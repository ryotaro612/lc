class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = dict()
        for i, c in enumerate(order):
            table[c] = i
        
        for i in range(len(words) - 1):
            word = words[i]
            word2 = words[i+1]
            ok = False
            for i in range(min(len(word), len(word2))):
                if table[word[i]] > table[word2[i]]:
                    return False
                elif table[word[i]] < table[word2[i]]:
                    ok = True
                    break
                    
            if ok is False and len(word) > len(word2):
                return False
            
        return True
