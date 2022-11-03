class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lst = sorted(arr, key = lambda e: (abs(x - e), e))
        return sorted(lst[:k])
