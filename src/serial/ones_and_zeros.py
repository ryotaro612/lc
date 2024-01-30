class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = dict()
        return self.rec(strs, 0, m, n, cache)

    def rec(self, strs, i, m, n, cache):
        key = (i, m, n)
        if key in cache:
            return cache[key]
        n_len = len(strs)
        if i == n_len:
            cache[key] = 0
            return cache[key]
        n_one = len([c for c  in strs[i] if c == '1'])
        n_zero = len([c for c in strs[i] if c == '0'])
        
        result = self.rec(strs, i+1, m, n, cache)
        if m >= n_zero and n >= n_one:
            result = max(result, 1 + self.rec(strs, i+1, m-n_zero, n - n_one, cache))
        cache[key] = result
        
        return cache[key] 
