import heapq

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mini = 0
        maxi = 0
        n = len(nums)
        prefix = [0] * (n+1)
        result = 0
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

            result = max(result, abs(prefix[i+1] - mini), abs(prefix[i+1] - maxi))
            maxi = max(prefix[i+1], maxi)
            mini = min(prefix[i+1], mini)
        
        return result
