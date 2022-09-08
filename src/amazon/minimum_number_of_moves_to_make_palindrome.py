from collections import defaultdict

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        cache = dict()
        return self.findMinCost(s, cache)
        
    def findMinCost(self, s, cache):
        if s in cache:
            return cache[s]
        n = len(s)
        if n <= 1:
            cache[s] = 0
            return cache[s]
        letter_pos = defaultdict(list)
        for i, c in enumerate(s):
            letter_pos[c].append(i)
        
        min_cost = float('inf')
        for positions in letter_pos.values():
            if len(positions) > 1:
                cost = positions[0] + n - 1  - positions[-1]
                min_cost = min(min_cost, cost)
        result = float('inf')
        for positions in letter_pos.values():
            if len(positions) > 1:
                cost = positions[0] + n - 1  - positions[-1]
                if min_cost == cost:
                    sub = s[:positions[0]] + s[positions[0]+1:positions[-1]] + s[positions[-1]+1:]
                    result = min(result, self.findMinCost(sub, cache) + cost)
                    break
        
        cache[s] = result
        return cache[s]
                    
