import heapq
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        mp = dict()
    
        for i, num in enumerate(nums):
            indice = num // (valueDiff + 1)

            if indice in mp:
                return True
            if abs(mp.get(indice+1, float('inf')) - num) <= valueDiff:
                return True
            if abs(mp.get(indice-1, float('inf')) - num) <= valueDiff:
                return True
            mp[indice] = num
            tail = i - indexDiff
            if tail >= 0:
                del mp[nums[tail] // (valueDiff + 1)]
        return False
