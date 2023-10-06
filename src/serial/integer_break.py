class Solution:
    def integerBreak(self, n: int) -> int:
        
        cache = dict()
        result = 0
        for v in range(1, n):
            result = max(result, self.calc(v, cache) * self.calc(n-v, cache))
        return result

    def calc(self, n, cache):
        if n in cache:
            return cache[n]
        if n <= 1:
            cache[n] = n
            return cache[n]
        
        result = n
        for v in range(1, n):
            left = self.calc(v, cache)
            right = self.calc(n-v, cache)

            result = max(result, left * right)
        cache[n] = result
        return cache[n]
