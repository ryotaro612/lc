from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        for v in counter.values():
            
            res += v * (v - 1) // 2

        return res 
