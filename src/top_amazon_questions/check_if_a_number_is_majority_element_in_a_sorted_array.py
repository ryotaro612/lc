import bisect
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = bisect.bisect_left(nums, target)
        if left == n or nums[left] != target:
            return False
        right = bisect.bisect_right(nums, target)
        # print(right -left)
        return (right - left) > n // 2
