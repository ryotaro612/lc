class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = dict()
        return self.rec(arr, 0, k, cache)

    def rec(self, arr, pos, k, cache):
        if pos in cache:
            return cache[pos]
        n = len(arr)
        if n <= pos:
            cache[pos] = 0
            return cache[pos]
        
        mx_val = 0
        result = 0
        for i in range(pos, min(pos+k, n)):
            mx_val = max(mx_val, arr[i])
            result = max(result, mx_val * (i+1-pos) + self.rec(arr, i+1, k, cache))
        cache[pos] = result
        return cache[pos]
