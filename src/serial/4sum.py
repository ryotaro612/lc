"""
[3,1,4,2,-2,-1]
2
Expected
[[-2,-1,1,4],[-2,-1,2,3]]


[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
200
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, 4, target)
    
    def kSum(self, nums: List[int], k, target: int):
        n = len(nums)
        if n < k:
            return []
        if k == 2:
            return self.twoSum(nums, target)
        result = []
        
        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                for subset in self.kSum(nums[i + 1:], k-1, target - nums[i]):
                    result.append([nums[i]] + subset)
#        for i in range(k-1, n):
#            if i == 0 or nums[i-1] != nums[i]:
#                for lst in self.kSum(nums[:i], k-1, target - nums[i]):
#                    lst.append(nums[i])
#                    result.append(lst)
#        print(k, result)
        return result
            
    def twoSum(self, nums: List[int], target):
        result = []       
        n = len(nums)
        l_i, h_i = 0, n-1
        while l_i < h_i:
            sum_v = nums[l_i] + nums[h_i]
            if sum_v < target:
                l_i += 1
            elif target < sum_v:
                h_i -= 1
            else:
                pair = [nums[l_i], nums[h_i]]
                if len(result) == 0 or result[-1] != pair:
                    result.append(pair)
                l_i += 1
        return result
