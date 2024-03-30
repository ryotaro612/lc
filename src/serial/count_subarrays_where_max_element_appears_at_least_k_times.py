class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        n_max = 0
        right = 0
        max_val = max(nums)
        n = len(nums)
        for left in range(n):
            right = max(left, right)

            while right < n and n_max < k:
                if nums[right] == max_val:
                    n_max += 1
                right += 1

            if n_max == k:
                result += n - right + 1

            if left < right and nums[left] == max_val:
                n_max -= 1

        return result 
