class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        result = []
        self.backtrack(word, result, 0, [], 0)
        return result
    def backtrack(self, word, result, pos, prefix, k):
        n = len(word)
        if pos == n:
            result.append(''.join(prefix) + (str(k) if k else ''))
            return
        
        if k:
            prefix.append(str(k))
            prefix.append(word[pos])
            self.backtrack(word, result, pos+1, prefix, 0)
            prefix.pop()
            prefix.pop()
        else:
            prefix.append(word[pos])
            self.backtrack(word, result, pos+1, prefix, 0)
            prefix.pop()
        
        self.backtrack(word, result, pos+1, prefix, k+1)
        
"""
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n =len(word)
        result = []

        for i in range(1<<n):
            abbr = []
            stack = []
            for j in range(n):
                if i & (1 << j):
                    stack.append(word[j])
                else:
                    if stack:
                        abbr.append(str(len(stack)))
                        stack = []
                    abbr.append(word[j])
            if stack:
                abbr.append(str(len(stack)))
            result.append(''.join(abbr))
        return result
"""
