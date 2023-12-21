class Solution:
    def integerReplacement(self, n: int) -> int:
        cache = dict()        
        return self.rec(n, cache)

    def rec(self, n, cache):
        if n in cache:
            return cache[n]
        
        if n == 1:
            return 0
        
        if n % 2:
            cache[n] = 1 + min(self.rec(n+1, cache), self.rec(n-1, cache))
        else:
            cache[n] = 1 + self.rec(n//2, cache)
        
        return cache[n]
        
