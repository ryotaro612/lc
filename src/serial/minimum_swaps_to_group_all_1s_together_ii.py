class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        nums += nums
        n = len(nums)

        prefix = [0] * (n+1)
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i]
            if num:
                prefix[i+1] += 1
        result = float('inf')
        n_ones = len([num for num in nums if num == 1]) // 2
        for i in range(n//2):
            result = min(result, n_ones - (prefix[i+n_ones] - prefix[i]))
        
        return result
