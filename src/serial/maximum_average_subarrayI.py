class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_window = sum(nums[:k])
        result = sum_window / k
        for i in range(k, len(nums)):
            sum_window -= nums[i-k]
            sum_window += nums[i]
            result = max(result, sum_window / k)
        return result
