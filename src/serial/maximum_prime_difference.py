class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        
        primes = self.get_primes(max(nums))
        n = len(nums)
        prime_idx = [i for i in range(n) if nums[i] in primes]

        return prime_idx[-1] - prime_idx[0]

    def get_primes(self, mx):
        prime = [True for _ in range(mx + 1)]
        prime[0] = False
        prime[1] = False
        result = set()
        for i in range(2, mx + 1):
            if not prime[i]:
                continue
            result.add(i)
            for j in range(i+i, mx+1, i):
                prime[j] = False
        
        return result
