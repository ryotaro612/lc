class Solution:
    def monkeyMove(self, n: int) -> int:
        result = 1
        x = 2
        mod = 10**9 + 7
        while n:
            if n & 1:
                result *= x
                result %= mod
            x *= x   
            x %= mod
            n >>= 1
        
        
        return (result - 2 + mod) % mod
