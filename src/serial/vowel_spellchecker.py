class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        KiTe -> k*t*
        {k*t* -> 0}
        """
        n = len(queries)
        result = [""] * n
        done = [False] * n

        words = set(wordlist)
        for i, query in enumerate(queries):
            if query in words:
                result[i] = query
                done[i] = True

        words = dict()
        for i, w in enumerate(wordlist):
            if w.upper() not in words:
                words[w.upper()] = i
        
        for i, query in enumerate(queries):
            if not done[i] and query.upper() in words:
                done[i] = True
                result[i] = wordlist[words[query.upper()]]

        spell = dict()
        for i, word in enumerate(wordlist):
            norm = self.normalize(word)
            if norm not in spell:
                spell[norm] = i
        
        for i, query in enumerate(queries):
            if done[i]:
                continue
            
            norm = self.normalize(query)
            if norm in spell:
                result[i] = wordlist[spell[norm]]
        
        return result

    def check(self, words, done, queries, result):
        for i, query in enumerate(queries):
            if not done[i] and query in words:
                result[i] = query
                done[i] = True
        

    def normalize(self, word):
        chars = []
        for c in word.lower():
            if c in "aeiou":
                chars.append('*')
            else:
                chars.append(c)
            
        norm = ''.join(chars)
        return norm
