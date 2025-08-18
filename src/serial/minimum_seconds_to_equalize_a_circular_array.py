from collections import defaultdict
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        pos = {}
        gap = defaultdict(int)
        for i, num in enumerate(nums + nums):
            if num in pos:
                gap[num] = max(gap[num], (i - pos[num]) // 2)
        
            pos[num] = i
        return min(gap.values())
