"""
12 = 2^2, 3^1
(2^1, 3^1)
[(2, 2), (3, 1)] = 2^2 * 3^1

[(2, 1), (3,1)] -> return 
[(2, 2), (3,0)]
"""
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        prime_factors = self.factorize(n)
        return self.compute_factors(prime_factors)
        
    def compute_factors(self, prime_factors):
        n = len(prime_factors)
        if n == 0:
            return []
        candidates = []
        remain = 0
        if sum([exp for _, exp in prime_factors]) == 2:
            result = []
            for prime, exp in prime_factors:
                if exp == 2:
                    return [[prime, prime]]
                elif exp == 1:
                    result.append(prime)
            return [sorted(result)]

        prime = prime_factors[-1][0]
        if prime_factors[-1][1] == 1:
            prime_factors.pop()
        else:
            prime_factors[-1] = (prime, prime_factors[-1][1] - 1)
        
        candidates = []
        patterns = self.compute_factors(prime_factors)
        for pattern in patterns:
            candidates.append(sorted([prime] + pattern))
            a = 1
            for v in pattern:
                a *= v
            candidates.append(sorted([prime, a]))
            for j in range(len(pattern)):
                cpy_pattern = list(pattern)
                cpy_pattern[j] *= prime
                candidates.append(sorted(cpy_pattern))
        candidates.sort()
        result = []
        for i in range(len(candidates)):
            if len(result) == 0:
                result.append(candidates[i])
            else:
                if result[-1] != candidates[i]:
                    result.append(candidates[i])
        return result        
        
    def factorize(self, n):
        orig = n
        result = dict()
        i = 2
        while i * i <= n:
            while n % i == 0:
                result[i] = 1 + result.get(i, 0)
                n //= i
            else:
                i += 1
               
        if n not in {1, orig}:
            result[n] = 1
        return [(p, f) for p, f in result.items()]
