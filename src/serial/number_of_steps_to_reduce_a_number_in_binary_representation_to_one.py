class Solution:
    def numSteps(self, s: str) -> int:
        seq = [int(c) for c in s]
        return self.rec(seq)
    
    def rec(self, seq):
        if seq == [1]:
            return 0
        if seq[-1] == 0:
            return 1 + self.rec(seq[:-1])
        
        n = len(seq)

        for i in range(n-1, -1, -1):
            if seq[i] == 0:
                seq[i] = 1
                return 1 + self.rec(seq)
            seq[i] = 0
        
        return 1 + self.rec([1] + seq)
