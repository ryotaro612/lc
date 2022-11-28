class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        for i in range(0, n, 2):
            result += nums[i]
            
        return result
