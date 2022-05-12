class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        found = bisect.bisect_left(nums, target)
        return found
