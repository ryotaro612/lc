class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        right = 0
        result = 0
        prod = 1
        n = len(nums)
        for left in range(n):
            right = max(right, left)

            while right < n and prod * nums[right] < k:
                prod *= nums[right]
                right += 1
            
            result += right - left
            if left < right:
                prod //= nums[left]

        return result
