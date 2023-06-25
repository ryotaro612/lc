class Solution:
    def expand(self, s: str) -> List[str]:
        words = dict()
        return sorted(self.build(s, 0, words))


    def build(self, s, i, words):
        # temp a pattern of s[:i]  ac b c
        if s[i:] in words:
            return words[s[i:]]

        if len(s) == i:
            return [""]
        
        if s[i] != '{':
            sub_words = self.build(s, i+1, words)
            words[s[i:]] = [s[i] + sub_word for sub_word in sub_words]
        else:
            j = i
            while s[j] != '}':
                j += 1
            letters = s[i+1:j].split(',')
            result = []
            
            for letter in letters:
                sub_words = self.build(s, j+1, words)
                result.extend([letter + sub_word for sub_word in sub_words])
            
            words[s[i:]] = result
            
        return words[s[i:]]
