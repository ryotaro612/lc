class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        erased = set()
        right = 0
        sum_window = 0
        for left in range(n):
            right = max(left, right)
            while right < n and nums[right] not in erased:
                sum_window += nums[right]
                erased.add(nums[right])
                right += 1

                result = max(result, sum_window)
            
            sum_window -= nums[left]
            erased.remove(nums[left])
        
        return result
