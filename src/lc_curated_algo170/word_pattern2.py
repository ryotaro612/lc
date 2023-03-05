"""
d
e

ab
aa
"""
from collections import defaultdict
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        return self.backtrack(pattern, s, 0, 1, dict(), 0)
    
    def backtrack(self, pattern, s, p_i, s_i, mapping: dict, left):
        # print(p_i,left, s_i, mapping)
        if len(pattern) == p_i and len(s) == left:
            # print(mapping, p_i, s_i)
            rev = defaultdict(set)
            for c, sub in mapping.items():
                rev[sub].add(c)
            # print(rev)
            return all(len(v) == 1 for v in rev.values())
        elif p_i < len(pattern) and s_i <= len(s):
            c = pattern[p_i]
            if c in mapping:
                sub =  mapping[c]
                return sub == s[left:left+len(sub)] and self.backtrack(pattern, s, p_i+1, left+len(sub)+1, mapping, left+len(sub))
            
            mapping[c] = s[left:s_i]
            if self.backtrack(pattern, s, p_i+1, s_i+1, mapping, s_i):
                return True
            del mapping[c]
            return self.backtrack(pattern, s, p_i, s_i+1, mapping, left)
