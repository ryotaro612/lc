from collections import defaultdict

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = defaultdict(int)
        for i, num in enumerate(nums):
            right[num] += 1

        result = 0
        mod = 10**9 + 7
        for num in nums:
            right[num] -= 1
            result += right[num*2] * left[num*2]
            result %= mod
            left[num] += 1
        
        return result
