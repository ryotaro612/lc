class Solution:
    def clumsy(self, n: int) -> int:
    
        i = n
        
        while i > 0:
            
            temp = i
            temp2 = 0
            if i - 1 > 0:
                temp *= i - 1
            if i - 2 > 0:
                temp //= i - 2
            if i - 3 > 0:
                temp2 = i - 3
            
            if i == n:
                res = temp + temp2
            else:
                res -= temp
                res += temp2
            i -= 4
        
        return res
            

