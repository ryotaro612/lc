class Solution:
    def __init__(self):

        self.dp = dict()

    def getKth(self, lo: int, hi: int, k: int) -> int:    
        return sorted([(self.power(v), v) for v in range(lo, hi+1)])[k-1][1]
    
    def power(self, v):
        if v in self.dp:
            return self.dp[v]
        
        result = 0

        while v != 1:
            if v % 2:
                v = 3 * v + 1
            else:
                v = v // 2
            result += 1
        
        self.dp[v] = result
        return result
