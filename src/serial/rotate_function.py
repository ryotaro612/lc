
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        Time Complexity O(n)
        Extra Space Complexity O(1)
        """
        cur = 0
        n = len(nums)
        for i in range(n):
            cur += i * nums[i]
        result = cur
        nums_sum = sum(nums)
        for i in range(n-1, -1, -1):
            cur += nums_sum - n * nums[i]
            result = max(result, cur)
        return result
