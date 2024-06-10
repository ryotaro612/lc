class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        n_b = len(b)
        n_a = len(a)

        ub = n_b // n_a + 3
        lb =  -1 

        while ub - lb > 1:
            mid = (ub + lb) // 2
            if (a * mid).find(b) != -1:
                ub = mid
            else:
                lb = mid
        
        if ub == n_b // n_a + 3:
            return -1
        return ub
        
