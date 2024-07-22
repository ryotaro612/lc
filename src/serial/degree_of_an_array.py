from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        num_pos = defaultdict(list)
        for i, num in enumerate(nums):
            num_pos[num].append(i)
        
        smallest = max([len(v) for v in num_pos.values()])
        result = float('inf')
        for v in num_pos.values():
            if len(v) == smallest:
                result = min(result, v[-1] - v[0] + 1)
        return result
            
