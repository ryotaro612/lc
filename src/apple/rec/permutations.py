
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        self.perm(0, nums, result)
        return result
        
    def perm(self, index, nums, result):
        n = len(nums)
        
        if index == n:
            result.append(nums[:])
            return
        
        for i in range(index, n):
            
            nums[i], nums[index] = nums[index], nums[i]
            self.perm(index+1, nums, result)
            nums[i], nums[index] = nums[index], nums[i]
            
