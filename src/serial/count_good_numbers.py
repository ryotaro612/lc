class Solution:
    def countGoodNumbers(self, n: int) -> int:
        """
        m
        0, 2, 4, 6, 8
        5**m + 4**(n-m)
        n, m
        1, 1
        2, 1
        3, 2
        4, 2
        5, 3
        m = (n+1)// 2
        """
        m = (n+1) // 2
        mod = 10**9 + 7
        res = self.my_pow(5, m, mod)
        if n - m:
            res *= self.my_pow(4, n-m, mod) 

        res %= mod
        return res
    

    def my_pow(self, x, a, mod):
        res = 1
        while a:
            if a & 1:
                res *= x
                res %= mod
            
            a = a >> 1
            x *= x
            x %= mod
            res %= mod
        
        return res
