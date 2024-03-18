from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = set()
        counter = Counter(nums)
        
        for num in nums:
            counter[num] -= 1
            if k == 0:
                if counter[num]:
                    result.add((num, num))
            else:
                if counter[num+k]:
                    result.add((num, num+k))
                if counter[num-k]:
                    result.add((num-k, num))
                    
        return len(result)
