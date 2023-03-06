"""
[1,2]
1
"""
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        v = 0
        for num in arr:
            while v < num and k:
                k -= 1
                v += 1
            if num == v:
                v += 1
        while k:
            k -= 1
            v += 1
        return v
