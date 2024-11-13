import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        result = 0
        nums.sort()
        [0, 1, 4, 4, 5, 7], 3, 6
        for i, num in enumerate(nums):

            left = bisect.bisect_left(nums, lower - num)
            right = bisect.bisect_right(nums, upper - num)
            result += right - left
            if left <= i < right:
                result -= 1

        return result // 2
