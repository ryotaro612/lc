from collections import defaultdict
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = defaultdict(int)
        for word in words:
            for c in word:
                freq[c] += 1
        
        n = len(words)
        for f in freq.values():
            if f % n:
                return False
        return True
