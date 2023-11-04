class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        l = max(left + [0])
        r = min(right + [float('inf')])
        return max(l, n - r)
