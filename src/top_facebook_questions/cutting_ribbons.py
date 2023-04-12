class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        n = len(ribbons)
        lb = 0
        ub = max(ribbons) + 1
        while ub -  lb > 1:
            mid = (ub + lb) // 2
            count = 0
            for ribbon in ribbons:
                count += ribbon // mid
            
            if count >= k:
                lb = mid
            else:
                ub = mid
        return lb
