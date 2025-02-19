class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        patterns = []
        self.rec([], n, patterns)
        if len(patterns) < k:
            return ""
        else:
            return patterns[k-1]
    
    def rec(self, temp, n, patterns):
        if len(temp) == n:
            patterns.append(''.join(temp))
            return
        
        cands = ['a', 'b', 'c']
        for cand in cands:
            if not temp or cand != temp[-1]:
                temp.append(cand)
                self.rec(temp, n, patterns)
                temp.pop()
        
