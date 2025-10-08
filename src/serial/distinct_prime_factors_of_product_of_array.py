from collections import defaultdict
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        """
        """
        primes = set()
        for num in nums:
            for p in self.find_primes(num):
                primes.add(p)

        return len(primes)

    def find_primes(self, num):
        i = 2
        freq = defaultdict(int)
        while i * i <= num:
            while num % i == 0:
                freq[i] += 1
                num //= i
            i += 1
        if num != 1:
            freq[num] += 1
        
        return list(freq.keys())
