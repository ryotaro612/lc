class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        bits = [-1] * 31
        n = len(nums)
        result = [-1] * n
        for i in range(n-1, -1, -1):
            k = i
            for j in range(31):
                if nums[i] & (1<<j):
                    bits[j] = i
                else:
                    if bits[j] >= 0:
                        k = max(k, bits[j])
            
            result[i] = k - i + 1
        
        return result
