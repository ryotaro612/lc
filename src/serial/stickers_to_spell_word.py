class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        counter = [0] * 26
        for c in target:
            counter[ord(c) - ord('a')] += 1
        counter = tuple(counter)

        cache = dict()
        res = self.rec(stickers, counter, 0, cache)
        return res if res < float('inf') else -1
    
    def rec(self, stickers, counter, i, cache):
        key = (counter, i)
        if key in cache:
            return cache[key]
        
        if counter == tuple([0] * 26):
            cache[key] = 0
            return cache[key]
        
        if len(stickers) == i:
            cache[key] = float('inf')
            return cache[key]

        res = float('inf')
        next_counter = list(counter)
        for j in range(16):
            res = min(res, j + self.rec(stickers, tuple(next_counter), i+1, cache))
            prev = list(next_counter)
            for c in stickers[i]:
                next_counter[ord(c) - ord('a')] = max(next_counter[ord(c) - ord('a')] - 1, 0) 
                
            if prev == next_counter:
                break
        cache[key] = res
        return res
