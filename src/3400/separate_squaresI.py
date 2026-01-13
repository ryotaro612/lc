class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        lb  = float('inf')
        ub = -float('inf')

        total = 0
        for x, y, l in squares:
            lb = min(lb, y)
            ub = max(ub, y + l)
        
        while ub - lb > 0.00001: 
            mid = (ub + lb) / 2
            ub_area = 0
            lb_area = 0
            for x, y, l in squares:
                if y >= mid:
                    ub_area += l * l
                elif y + l <= mid:
                    lb_area += l * l
                else:
                    ub_area += l * (l - (mid - y))
                    lb_area += l * (mid - y)

            if ub_area <= lb_area:
                ub = mid
            else:
                lb = mid
        
        return ub
