"""
m - 1 + n - 1 = n + m - 2
(n + m -2, n - 1)

"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        numerator = 1
        # [n+m - 2 - (n-1 + 1), .. n + m - 2]
        for i in range((n+m-2) - (n-1) + 1, (n+m-2) + 1):
            numerator *= i
            
        denom = 1
        for i in range(1, n - 1 + 1):
            denom *= i
            
        return numerator // denom
