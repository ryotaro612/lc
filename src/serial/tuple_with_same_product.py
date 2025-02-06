from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                counter[nums[i] * nums[j]] += 1
        
        result = 0
        for v in counter.values():
            result += v * (v-1) // 2 * 8
        return result
