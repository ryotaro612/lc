"""
["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
[[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
"""
class WordDictionary:

    def __init__(self):
        self.trie = dict()
        

    def addWord(self, word: str) -> None:
        node = self.trie
        for i, c in enumerate(word):
            if c not in node:
                node[c] = dict()
            node = node[c]
            if i == len(word) - 1:
                node['_'] = None
            
    def search(self, word: str) -> bool:
        # print(word, '!!')
        return self._search(self.trie, 0, word)
    
    def _search(self, node, pos, word):
        # print(node, '!')
        if pos == len(word):
            return '_' in node
        c = word[pos]
        if c == '.':
            for child in node:
                if child != '_' and self._search(node[child], pos+1, word):
                    return True
            return False
        
        if c in node:
            return self._search(node[c], pos+1, word)
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
