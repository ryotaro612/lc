from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        prefix_sum = defaultdict(list)
        prefix_sum[v]  = nums of i
        
        result = 0
        for i in range(len(nums)):
            cur_prefix = sums(nums[:i+1])
            prefix_sum[cur_prefix] -= 1
            result += prefix_sum[cur_prefix+goals]
            
        return result 
        """
        cur_sum = 0
        n = len(nums)
        prefix_sum_count = defaultdict(int)
        for num in nums:
            cur_sum += num
            prefix_sum_count[cur_sum] += 1
        
        result = 0

        cur_sum = 0
        for i, num in enumerate(nums):
            result += prefix_sum_count[cur_sum + goal]
            cur_sum += num
            prefix_sum_count[cur_sum] -= 1
        
        return result
