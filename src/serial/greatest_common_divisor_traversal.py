class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        pars = [-1] * n
        divisor_id = dict()
        for i, num in enumerate(nums):
            for divisor in self.find_divisors(num):
                if divisor in divisor_id:
                    self.unite(divisor_id[divisor], i, pars)
                
                divisor_id[divisor] = i    

        return -pars[self.find_root(0, pars)] == n

    def find_root(self, i, pars):
        if pars[i] < 0:
            return i
        pars[i] = self.find_root(pars[i], pars)
        return pars[i]
    
    def is_same_group(self, a, b, pars):
        return self.find_root(a, pars) == self.find_root(b, pars)
    
    def unite(self, a, b, pars):
        if self.is_same_group(a, b, pars):
            return
        root_a = self.find_root(a, pars)
        root_b = self.find_root(b, pars)
        if pars[root_a] < pars[root_b]:
            pars[root_a] += pars[root_b]
            pars[root_b] = root_a
        else:
            pars[root_b] += pars[root_a]
            pars[root_a] = root_b
    
    def find_divisors(self, n):
        result = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                result.append(i)
                if n // i != i:
                    result.append(n//i)
            i += 1
        return result[1:]
        
