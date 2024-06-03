class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        right = 0
        result = 0
        for left in range(n):
            right = max(left, right)
            
            while right < n and (left == right or nums[right-1] < nums[right]):
                right += 1
            
            result = max(result, right - left)
        
        return result
