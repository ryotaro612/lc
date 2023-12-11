from collections import defaultdict
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        size = n // 4
        freq =defaultdict(int)
        for i in range(n):
            if arr[i] == arr[i+size]:
                return arr[i]
