import math
from collections import defaultdict
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        counter = defaultdict(int)

        nums.sort()
        for num in nums:
            sq = int(math.sqrt(num))
            if sq **2 == num:
                counter[num] = max(counter[num], counter[sq] + 1)
            else:
                counter[num] = 1
    
        result = -1
        if len(counter):
            result = max(counter.values())
        if result > 1:
            return result
        return -1
