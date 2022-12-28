class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp = dict()
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        for symbol, word in zip(pattern, words):
            if symbol in mp:
                if mp[symbol] != word:
                    return False
            else:
                mp[symbol] = word
        return len(set(mp.keys())) == len(set(mp.values()))
