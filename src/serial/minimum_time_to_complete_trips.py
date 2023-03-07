class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lb = 0
        ub = totalTrips * max(time) + 1
        while ub - lb > 1:
            mid = (ub + lb) // 2

            count = 0

            for bus in time:
                count += mid // bus
            
            if count < totalTrips:
                lb = mid
            else:
                ub = mid
        
        return ub
