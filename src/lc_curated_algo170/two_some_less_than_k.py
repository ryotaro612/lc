class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = -1
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] < k:
                    result = max(nums[i] + nums[j], result)
        
        return result
