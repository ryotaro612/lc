class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        result = 0
        for num in nums:
            if num - 1 not in num_set:
                val = num
                while val in num_set:
                    val += 1
                result = max(result, val - num)
        
        return result
