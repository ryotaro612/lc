from collections import Counter
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        res = 1
        counter = Counter(min(a, len(arr)) for a in arr)
        for i in range(2, len(arr)+1):
            res = min(res + counter[i], i)
        return res
