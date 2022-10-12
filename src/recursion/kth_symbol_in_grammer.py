"""
n, k

n-1, k / 2

[0]
0[1]
01[1]0
0110[1]001
n=4 k = 5
n=3,k= 4
n=2, k = 4/2 = 2
n=1, k = 2/2 = 1
n=0 , k = 0

"""
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return self.findVal(n-1, k-1)
    
    def findVal(self, n, k):
        if n == 0:
            assert k == 0
            return 0
        prev = self.findVal(n - 1, k // 2)
        if prev:
            if k % 2:
                return 0
            else:
                return 1
        else:
            if k % 2:
                return 1
            else:
                return 0
        
