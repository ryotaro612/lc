class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [nums[0]] * n
        
        for i in range(1, n):
            result[i] = result[i-1] + nums[i]

        return result
