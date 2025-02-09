from collections import defaultdict
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)
        freq[nums[0]] = 1
        result = 0
        for i in range(1, n):
            result += freq[nums[i] - i]
            freq[nums[i]-i] += 1
        
        return n * (n-1) // 2 - result
