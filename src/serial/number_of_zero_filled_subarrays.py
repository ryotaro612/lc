class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        len_zero = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                len_zero += 1
            if i == n - 1 or nums[i+1] != 0:
                result += len_zero * (len_zero - 1) // 2 + len_zero
                len_zero = 0
        return result
