class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = -1
        for i in range(n):
            for j in range(i+1, n):
                result = max(result, (nums[i]-1) * (nums[j]-1))
        return result
