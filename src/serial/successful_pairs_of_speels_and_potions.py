class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        result = []
        m = len(potions)
        for spell in spells:
            lb, ub = -1, m
            while ub - lb > 1:
                mid = (lb + ub) // 2
                if spell * potions[mid] >= success:
                    ub = mid
                else:
                    lb = mid
            result.append(m - ub)
        return result
