class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        ub, lb = n + 1, -1
        while ub - lb > 1:
            mid = (ub + lb) // 2

            count = len([c for c in citations if c >= mid])

            if count < mid:
                ub = mid
            else:
                lb = mid
        return lb
