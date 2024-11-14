class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        ub = max(quantities) + 1
        lb = -1
        while ub - lb > 1:
            mid = (ub + lb) // 2
            temp = list(quantities)
            
            for _ in range(n):
                if temp:
                    temp[-1] -= mid
                    if temp[-1] <= 0:
                        temp.pop()
                else:
                    break
            if temp:
                lb = mid
            else:
                ub = mid
        return ub
