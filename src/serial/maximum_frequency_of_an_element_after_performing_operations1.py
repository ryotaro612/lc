from collections import defaultdict

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        """
        nums[i]
        nums[i] -k <= nums[i] + k
        i+1
        """
        result = 0
        left = right = 0
        n = len(nums)
        for v in range(max(nums)+1):
            while nums[left] < v - k:
                left += 1
            while right < n - 1 and nums[right+1] <= v + k:
                right += 1
            if v < nums[left]:
                continue
            total = right - left + 1
            result = max(result, counter[v] + min(total - counter[v], numOperations))
        return result
