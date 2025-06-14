import math
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        xy = defaultdict(lambda: -math.inf)

        n = len(x)
        for i in range(n):
            xy[x[i]] = max(xy[x[i]], y[i])
        
        if len(xy) < 3:
            return -1
        
        vals = sorted(list(xy.values()), reverse=True)
        return sum(vals[:3])
