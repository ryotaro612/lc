import math
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 0
        mini = nums[0]
        for num in nums[1:]:
            if num - mini > k:
                result += 1
                mini = num
        return result + 1
