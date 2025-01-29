class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        found = {0: 0}
        result = 0 
        total = 0
        for num in nums:
            total += num
            if total - target in found:
                result = max(result, found[total-target] + 1)
            
            found[total] = result
        
        return result
