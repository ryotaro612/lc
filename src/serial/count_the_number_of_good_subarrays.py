from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int: 
        right = 0
        n = len(nums)
        counter = defaultdict(int)
        n_pairs = 0
        result = 0

        for left in range(n):
            right = max(left, right)

            while right < n and n_pairs < k:
                counter[nums[right]] += 1
                n_pairs += counter[nums[right]] - 1
                right += 1
                
            if n_pairs >= k:
                result += n - right + 1
            
            n_pairs -= counter[nums[left]] - 1
            counter[nums[left]] -= 1
        
        return result
             
        """
        [left, right)
        counter
        result = 0
        result += n - right + 1
        """
