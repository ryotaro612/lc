class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        """
        """
        n = len(s)
        lb = -1
        ub = n
        while ub - lb > 1:
            mid = (ub + lb) // 2
            stars = sorted([e for e in order[:mid+1]])
            
            if stars:
                stars = [-1] + stars + [n]
                counter = 0
                for i in range(1, len(stars)):
                    length = stars[i] - stars[i-1] - 1
                    counter += length * (length-1) // 2 + length
            else:
                counter = n * (n-1) // 2 + n
                 
            if n * (n-1) // 2 + n - counter >= k:
                ub = mid
            else:
                lb = mid
        if ub == n:
            return -1
        else:
            return ub
