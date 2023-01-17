class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.is_surjective(s, t) and self.is_surjective(t, s)
    
    def is_surjective(self, s, t):
        mp = dict()
        for i, c in enumerate(s):
            if c in mp:
                if mp[c] != t[i]:
                    return False
            else:
                mp[c] = t[i]
        return True
