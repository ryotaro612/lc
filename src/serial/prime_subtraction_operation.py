class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        cands = [True] * (max(nums) + 1)
        cands[0] = False
        cands[1] = False
        for i in range(2, len(cands)):
            if cands[i]:
                for j in range(i+i, len(cands), i):
                    cands[j] = False
        primes = []
      
        for i in range(len(cands)):
            if cands[i]:
                primes.append(i)
        
        
        for i in range(len(nums)):
            if i == 0:
                cand = nums[0]
                for prime in primes:
                    if prime < nums[0] and nums[0] - prime < cand:
                        cand = nums[0] - prime
                
                nums[0] = cand
            else:
                cand = nums[i]
                for prime in primes:
                    if prime < nums[i] and nums[i-1] < nums[i] - prime < cand:
                        cand = nums[i] - prime
                

                if cand <= nums[i-1]:
                    return False
                nums[i] = cand
        
        return True

