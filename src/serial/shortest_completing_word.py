from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        counter = Counter([c.lower() for c in licensePlate if c != ' ' and not c.isdigit()])
        
        res = None
        for word in words[::-1]:
            c = Counter(word)
            ok = True
            for k in counter:
                if not (k in c and counter[k] <= c[k]):
                    ok = False
            if ok:        
                if not res or len(res) >= len(word):
                    res = word
        return res
