from collections import defaultdict
class Solution:
    def longestDupSubstring(self, s: str) -> str:        
        n = len(s)
        ub = n
        lb = 0
        while ub - lb > 1:
            mid = (lb + ub) // 2
            found = self.find(mid, s)
            # print(mid, found)
            if found:
                lb = mid
            else:
                ub = mid
        
        return self.find(lb, s)
    
    def find(self, size, s):
        base = 10**8 + 7
        mod = 1 << 63
        reduce = base ** (size - 1)
        reduce %= mod

        h = 0
        for i in range(size):
            h *= base
            h %= mod
            h += ord(s[i])
            h %= mod
        hash_pos = defaultdict(list)
        hash_pos[h].append(0)
        i = 1
        
        while i + size <= len(s):
            
            h -= ord(s[i-1]) * reduce
            if h < 0:
                h += mod
            h *= base
            h %= mod
            h += ord(s[i+size-1])
            h %= mod
            hash_pos[h].append(i)
            i += 1
        for key in hash_pos:
            if len(hash_pos[key]) > 1:
                start = hash_pos[key][0]
                return s[start:start+size]
        return ""
