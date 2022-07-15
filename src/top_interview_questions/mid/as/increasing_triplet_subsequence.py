"""
[1 2 3 4 5]
nums[0] < nums[1] < nums[2]
i < j i.e. nums[i] < nums[j]
i < j i.e. nums[i] >= nums[j]
items = []
items[0] < items[1] < items[2]
"""
import bisect
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        items = []
        for num in nums:
            i = bisect.bisect_left(items, num)
            if i < len(items):
                items[i] = num
            else:
                items.append(num)
            items = items[:3]
        return len(items) == 3
