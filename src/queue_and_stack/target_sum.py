"""
[1,0]
1

[29,6,7,36,30,28,35,48,20,44,40,2,31,25,6,41,33,4,35,38]
35
"""
from collections import defaultdict, Counter

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        return self.count(nums, 0).get(target, 0)
    
    def count(self, nums, i):
        n = len(nums)
        if i == n - 1:
            return Counter([nums[n-1], -nums[n-1]])
            
        child = self.count(nums, i+1)
        res = defaultdict(int)
        for v in [-nums[i], nums[i]]:
            for k in child:
                res[k + v] += child[k]
        
        return res
