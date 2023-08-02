class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        factors = []
        while i**2 <= n:
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n//i)
            i += 1
        factors = sorted(factors)
        if len(factors) >= k:
            return factors[k-1]
        else:
            return -1
