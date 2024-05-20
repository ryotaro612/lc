class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for mask in range(1<<n):
            val = 0
            for i in range(n):
                if mask & (1<<i):
                    val ^= nums[i]
            
            result += val
        
        return result
