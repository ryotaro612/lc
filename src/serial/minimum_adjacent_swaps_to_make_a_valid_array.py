class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        max_v, min_v = max(nums), min(nums)
        n = len(nums)
        for i in range(n):
            if max_v == nums[i]:
                max_i = i
            if min_v == nums[n-1-i]:
                min_i = n-1-i

        if max_i < min_i:
            return n - 1 - max_i + min_i - 1
        else:
            return n-1 - max_i + min_i            
