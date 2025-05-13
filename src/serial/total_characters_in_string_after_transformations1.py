
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cache = dict()

        result = 0
        mod = 10**9 + 7
        
        for c in s:
            result += self.count(c, t, cache)
            result %= mod
        return result
        
    def count(self, c, t, cache):
        key = (c, t)
        if key in cache:
            return cache[key]
        
        if t <= 0:
            cache[key] = 1
            return 1
        
        mod = 10**9 + 7
        if c == 'z':
            cache[key] = (self.count('a', t-1, cache) + self.count('b', t-1, cache)) % mod
            return cache[key]
        
        
        step = ord('z') - ord(c)
        return self.count('z', t-step, cache)
    
        
