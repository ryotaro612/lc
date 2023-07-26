"""
[1,1,100000] 2.01
[1,1] 1
"""
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        inf = 10000000000
        lb, ub = 0, inf
        # print(lb, ub)
        while ub - lb > 1:
            mid = (ub + lb) // 2
            time = 0
            n = len(dist)
            for i, d in enumerate(dist):
                if i < n - 1:
                    if d % mid:
                        time += int(d / mid) + 1
                    else:
                        time += d // mid
                else:
                    time += d / mid
            
            
            if hour < time:
                lb = mid
            else:
                ub = mid
        if ub == inf:
            return -1
        else:
            return ub
