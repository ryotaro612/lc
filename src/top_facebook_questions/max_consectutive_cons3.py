"""
pos_zeros = []
if pos_zeros is empty:
    return len(nums)

if len(pos_zeros) <= k:
    return len(nums)


set pos_zeros[i] to 1 
pos_zeros[i+1] - pos_zeros[i-1] - 1


pos[i], pos[i+1]
pos_zeros[i+2] - pos_zeros[i-1] - 1
"""
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
        
#         positions = [-1] + [i for i, num in enumerate(nums) if num == 0] + [len(nums)]
        
#         if len(positions) <= k+2:
#             return len(nums)
#         # print(positions)
#         result = 0
#         i = 0
#         while i + k + 1 < len(positions):
#             result = max(result, positions[i+k+1] - positions[i] - 1)
#             i+=1
#         return result



"""
[1,1,1,0,0,0,1,1,1,1,0]
2
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        for right in range(len(nums)):
            
            if nums[right] == 0:
                k -= 1
            
            
            if k < 0:
                k += 1- nums[left]
                left += 1
        
        return right - left + 1    
