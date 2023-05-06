import bisect


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        mod = 10**9 + 7
        n = len(nums)
        for i, num in enumerate(nums):
            mx = target - num
            if num <= mx:
                j = bisect.bisect_right(nums, mx)
                result += 2 ** (j - 1 - i)
                result %= mod

        return result
