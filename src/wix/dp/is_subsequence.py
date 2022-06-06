class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps, pt = 0, 0
        n_s, n_t = len(s), len(t)
        
        while ps < n_s and pt < n_t:
            if s[ps] == t[pt]:
                ps += 1
            pt += 1
        
        return n_s <= ps
