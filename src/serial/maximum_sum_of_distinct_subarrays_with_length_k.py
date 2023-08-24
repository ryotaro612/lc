from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        freq = defaultdict(int)
        n_duplicate = 0
        result = 0
        sum_window = 0
        for i, num in enumerate(nums):
            sum_window += num
            
            if freq[num]==1:
                n_duplicate += 1
            freq[num] += 1
            if i >= k:
                tail = nums[i - k]
                if freq[tail] == 2:
                    n_duplicate -= 1
                freq[tail] -= 1
                sum_window -= tail
            if i >= k - 1 and n_duplicate == 0:
                result = max(result, sum_window)
        return result

