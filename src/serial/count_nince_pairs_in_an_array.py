from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        """
        counter = defaultdict(int)
        result = 0
        mod = 10**9 + 7
        for i in range(len(nums)):
            rev = int(str(nums[i])[::-1])
            key = nums[i] - rev
            result += counter[key]
            result %= mod
            counter[key] += 1
        return result
