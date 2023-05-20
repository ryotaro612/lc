class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        pos_zeros = [i for i, num in enumerate(nums) if num == 0]
        if len(pos_zeros) == 0:
            return len(nums)  - 1

        result = 0
        pos_zeros = [-1] + pos_zeros + [len(nums)]
        for i, pos in enumerate(pos_zeros):
            if i in {0, len(pos_zeros)-1}:
                continue
            
            result = max(result, pos_zeros[i] - pos_zeros[i-1] - 1 + pos_zeros[i+1] - pos_zeros[i] - 1)
        
        return result
            
