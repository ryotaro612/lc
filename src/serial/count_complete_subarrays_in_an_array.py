from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        result = 0
        right = 0
        n = len(nums)
        n_distinct = len(set(nums))
        counter = defaultdict(int)
        for left in range(n):
            right = max(left, right)
            while right < n and len(counter) < n_distinct:
                counter[nums[right]] += 1
                right += 1
            
            if len(counter) == n_distinct:
                result += n - right + 1
            
            counter[nums[left]] -= 1
            if counter[nums[left]] == 0:
                del counter[nums[left]]
        
        return result
