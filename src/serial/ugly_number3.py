class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l_ab = self.lcm(a,b)
        l_ac = self.lcm(a,c)
        l_bc = self.lcm(b, c)
        l_abc = self.lcm(self.lcm(a, b), c)
        
        ub = a * n + 1
        lb = 0
        while ub - lb > 1:
            pivot = (ub + lb) // 2
            count = pivot // a + pivot // b + pivot // c - pivot // l_ab - pivot // l_ac - pivot // l_bc + pivot // l_abc
            if count < n:
                lb = pivot
            else:
                ub = pivot
        
        return ub
    
    def lcm(self, a, b):
        return a * b // self.gcd(a, b)

    def gcd(self, a, b):
        if a < b:
            a, b = b, a
        
        if b == 0:
            return a
        
        return self.gcd(b, a % b)
