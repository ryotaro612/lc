from collections import defaultdict
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_map = defaultdict(list)
        for num in nums:
            total = 0
            for a in str(num):
                total += ord(a) - ord('0')
            digit_map[total].append(num)
        
        result = -1
        for v in digit_map.values():
            if len(v) <= 1:
                continue
            v.sort(reverse=True)
            result = max(result, v[0] + v[1])
        
        return result
