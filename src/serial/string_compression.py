class Solution:
    def compressedString(self, word: str) -> str:
        result = []

        word = [c for c in word]
        n = len(word)
        i = 0
        while i < n:
            counter = 1
            while i < n - 1 and counter < 9 and word[i] == word[i+1]:
                i += 1
                counter += 1
            
            result.extend([str(counter), word[i]])
            i += 1
        
        return ''.join(result)
