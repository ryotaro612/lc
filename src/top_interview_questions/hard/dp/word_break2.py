"""
memo[pos] = rec(pos, wordDict)
def rec(pos, memo, s, wordDict) -> list[list[str]] result of s[pos:]

s.startsWith(wordDict[3], pos) -> True

s[pos:pos+len(wordDict[3])]
rec(pos + len(wordDict[3]), memo, s, wordDict)
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = dict()
        result = self.rec(0, memo, s, set(wordDict))
        # print(memo)
        return result
    def rec(self, pos, memo, s, wordDict):
        n = len(s)
        if pos >= n:
            return []
        if pos in memo:
            return memo[pos]
        
        result = []
        for i in range(pos+1, n+1):
            word = s[pos:i]
            if word in wordDict:
                # print(word, s[pos:])
                word_n = len(word)
                sub_sentences = self.rec(pos+word_n, memo, s, wordDict)
                if len(sub_sentences) > 0:
                    for sentence in sub_sentences:
                        result.append(word + ' ' + sentence)
                elif pos+word_n == n:
                    result.append(word)
        memo[pos] = result
        return result
