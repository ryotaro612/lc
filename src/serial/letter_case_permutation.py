class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        cache = dict()

        return self.rec(cache, 0, s)

    def rec(self, cache, i, s):
        if i in cache:
            return cache[i]

        n = len(s)
        if i == n:
            cache[n] = [""]
            return cache[n]
        
        result = []
        patterns = self.rec(cache, i+1, s)

        prefix = [s[i]]
        if s[i].isupper():
            prefix.append(s[i].lower())
        elif s[i].islower():
            prefix.append(s[i].upper())
        
        
        for c in prefix:
            for pattern in patterns:
                result.append(c + pattern)
        
        return result
