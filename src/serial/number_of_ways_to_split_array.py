class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        result = 0
        prefix = 0
        total = sum(nums)
        n = len(nums)
        for i in range(n-1):
            prefix += nums[i]
            if prefix >= total - prefix:
                result += 1
        
        return result
