class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        n = len(weights)
        ub, lb = sum(weights) + 1, max(weights) - 1
        while ub - lb > 1:
            mid = (ub+lb) // 2

            running_days = 0
            used = 0
            for weight in weights:
                if used + weight > mid:
                    running_days += 1
                    used = 0
                used += weight
                
            if weight:
                running_days += 1
            
            if running_days > days:
                lb = mid
            else:
                ub = mid
        return ub
