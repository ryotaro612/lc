class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = k * 2 + 1
        result = [-1] * n
        if n < window:
            return result
        sub_sum = sum(nums[:window])
        result[k] = self.average(sub_sum, window)
        for i in range(k + 1, n - k):
            sub_sum -= nums[i - k - 1]
            sub_sum += nums[i + k]
            result[i] = self.average(sub_sum, window)
        return result
