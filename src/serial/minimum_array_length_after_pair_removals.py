from collections import Counter
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        counter = Counter(nums)

        n = len(nums)

        maxi = max(counter.values())

        if maxi <= n//2:
            if n % 2:
                return 1
            
            return 0

        return maxi - (n- maxi)    
