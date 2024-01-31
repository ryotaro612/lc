import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        result = 0

        for house in sorted(houses):
            i = bisect.bisect_left(heaters, house)
            cand = float('inf')
            if i < len(heaters):
                cand = heaters[i] - house
            if i:
                cand = min(cand, house - heaters[i-1])
            result = max(result, cand)
        
        return result
