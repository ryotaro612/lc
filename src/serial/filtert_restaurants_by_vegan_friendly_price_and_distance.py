class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        result = []
        for r in restaurants:
            if veganFriendly:
                if r[2] == 0:
                    continue
            if r[3] > maxPrice:
                continue
            if r[4] > maxDistance:
                continue
            
            result.append(r)
        
        return [r[0] for r in sorted(result, key=lambda r: (-r[1], -r[0]))]
