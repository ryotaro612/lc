class Solution:
    def minOperations(self, n: int) -> int:
        result = 0
        i = 0
        # print(bin(n))
        while (n >> i):
            if (n>>i) & 3 == 3:
                n += (1 << i)
                result += 1
            i += 1
        
        i = 0
        while (n >> i):
            if 1 & (n >> i):
                result += 1
            i += 1
        return result
                
