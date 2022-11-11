"""
"cba"
"abcd"

"cbafg"
"abcd"
"""
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        lst = list(s)
        
        d = dict()
        for i, c in enumerate(order):
            d[c] = i
        
        for i in range(26):
            c = chr(i + ord('a'))
            if c not in d:
                d[c] = 26
        
        return ''.join(sorted(lst, key = lambda c: d[c]))
