class Solution:
    def queryString(self, s: str, n: int) -> bool:
        n_s = len(s)

        if n_s < n:
            return False
        
        for i in range(1,n+1):
            if s.find(str(bin(i))[2:]) == -1:
                return False
        
        return True
