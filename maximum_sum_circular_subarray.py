"""
[-5,-2,5,6,-2,-7,0,2,8]
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        
        
        result = self.kadane(nums)
        if len(nums) == 1:
            return result
        
        total = sum(nums)
        
        result = max(result, total + self.kadane([-num for num in nums[1:]]))
        result = max(result, total + self.kadane([-num for num in nums[:-1]]))
        return result 
    
    def kadane(self, nums):
        result = 0
        total = 0
        for num in nums:
            total =  num + max(0, total)
            result = max(total, result)
        return result
                
