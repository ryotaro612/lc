class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        mask |= num[right]

        mums[left]
        result = 1
        """
        mask = right = 0
        result = 1
        n = len(nums)
        for left in range(n):
            right = max(left, right)
            while right < n and (mask & nums[right] == 0):
                mask |= nums[right]
                right += 1
                result = max(result, right - left)
            mask ^= nums[left]
        
        return result
