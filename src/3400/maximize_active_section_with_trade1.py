from itertools import groupby, pairwise
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        lst = [len(list(c)) for a, c in groupby(s) if a == '0']
        
        cnt = s.count('1')
        return cnt + max([a+b for a, b in pairwise(lst)], default=0)
