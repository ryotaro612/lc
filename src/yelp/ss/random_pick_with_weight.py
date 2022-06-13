"""
Solution([1, 3, 4]);
0 + 1, 1 + 3,  4 + 4
prefix_sum = [1, 4, 8]
"""
import random
class Solution:

    def __init__(self, w: List[int]):
        buckets = []
        v = 0
        for item in w:
            if len(buckets) == 0:
                buckets.append(item)
            else:
                buckets.append(item + buckets[-1])
        self.buckets = buckets
    def pickIndex(self) -> int:
        value = random.randrange(0, self.buckets[-1])
        lb, ub = -1, len(self.buckets)
        while ub - lb > 1:
            mid = (ub + lb) // 2
            if value < self.buckets[mid]:
                ub = mid
            else: #self.buckets[mid] <= value
                lb = mid
        # print(value, ub)
        return ub
            
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
