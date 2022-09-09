"""
["a","b","c"]
"aadsfasf absbs bbab cadsfafs"
"""
from collections import defaultdict

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = dict()
        for word in dictionary:
            node = trie
            for i, c in enumerate(word):
                if c not in node:
                    node[c] = dict()
                node = node[c]
                
                if i == len(word) - 1:
                    node['*'] = True
        tokens = sentence.split(' ')
        
        for i in range(len(tokens)):
            word = tokens[i]
            node = trie
            found = []
            for j, c in enumerate(word):
                if c in node:
                    found.append(c)
                    node = node[c]
                    if '*' in node:
                        tokens[i] = ''.join(found)
                        break
                else:
                    break
        return ' '.join(tokens)
