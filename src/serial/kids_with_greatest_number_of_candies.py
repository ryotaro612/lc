class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for candy in candies:
            if candy == max_candies or candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result
