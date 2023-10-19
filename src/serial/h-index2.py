class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lb = -1
        ub = len(citations)
        n = len(citations)

        while ub - lb > 1:
            mid = (ub + lb) // 2
            if citations[mid] >= n - mid:
                ub = mid
            else:
                lb = mid
        if ub < 0:
            return n
        return n - ub
