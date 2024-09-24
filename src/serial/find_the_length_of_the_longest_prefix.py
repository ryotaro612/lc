class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = dict()
        for d in arr1:
            s = str(d)
            node = trie
            for c in s:
                if c not in node:
                    node[c] = dict()
                node = node[c]
        
        result = 0
        for e in arr2:
            s = str(e)
            counter = 0
            node = trie
            for i, c in enumerate(s):
                if c in node:
                    node = node[c]
                    counter += 1
                    result = max(result, counter)
                else:
                    break
        return result
            
