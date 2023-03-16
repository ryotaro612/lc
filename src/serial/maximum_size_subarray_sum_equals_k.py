class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix = {0: -1}
        n = len(nums)
        running_sum = 0
        result = 0
        for i, num in enumerate(nums):
            running_sum += num
            if running_sum - k in prefix:
                result = max(result, i - prefix[running_sum - k])
            if running_sum not in prefix:
                prefix[running_sum] = i
        return result
