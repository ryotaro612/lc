from collections import defaultdict
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for left, num in enumerate(nums):
            distinct = set()
            n_odd = 0
            for right in range(left, n):
                if nums[right] not in distinct:
                    if nums[right] % 2:
                        n_odd += 1
                    distinct.add(nums[right])
                
                if len(distinct) == n_odd * 2:
                    result = max(result, right - left + 1)
            
        return result
        
