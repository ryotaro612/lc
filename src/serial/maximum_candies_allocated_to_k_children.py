class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        mid

        if candy >= mid
            result += candy // mid
        result < k
        ub = mid
        lb = mid

        lb
        """
        lb = 0 
        ub = max(candies) + 1
        while ub - lb > 1:
            mid = (ub + lb) // 2
            counter = 0
            for candy in candies:
                if candy >= mid:
                    counter += candy // mid
            if counter < k:
                ub = mid
            else:
                lb = mid
        
        return lb
