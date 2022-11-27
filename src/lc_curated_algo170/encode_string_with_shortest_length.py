"""
"aabcaabcd"

"""
class Solution:
    def encode(self, s: str) -> str:
        
        memo = dict()
        return self.enc(s, memo)
    
    def enc(self, s, memo):
        if s in memo:
            return memo[s]
        
        pos = (s + s).find(s, 1)
        
        cands = [s]
        n = len(s)
        if pos < n:
            freq = n // pos
            cands.append(f"{freq}[{self.enc(s[:pos], memo)}]")
            
        for i in range(1, n):
            cands.append(self.enc(s[:i], memo) + self.enc(s[i:], memo))
        
        # print(s,pos, cands)
        memo[s] = sorted(cands, key=lambda x: len(x))[0]
    
        return memo[s]
     
"""
def encode(self, s, memo={}):
    if s not in memo:
        n = len(s)
        i = (s + s).find(s, 1)
        one = '%d[%s]' % (n / i, self.encode(s[:i])) if i < n else s
        multi = [self.encode(s[:i]) + self.encode(s[i:]) for i in xrange(1, n)]
        memo[s] = min([s, one] + multi, key=len)
    return memo[s]
"""
