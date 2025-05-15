from collections import defaultdict
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        """
        occupied = pos -> bool
        """
        occupied = defaultdict(lambda : False)

        for num in nums:
            occupied[num] = True
        
        n = len(moveFrom)
        for i in range(n):
            if occupied[moveFrom[i]]:
                occupied[moveFrom[i]] = False
                occupied[moveTo[i]] = True
        
        return sorted([i for i, e in occupied.items() if e])
