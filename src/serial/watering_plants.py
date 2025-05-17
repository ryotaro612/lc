class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 1
        water = capacity - plants[0]
        n = len(plants)
        for i in range(1, n):
            if water < plants[i]:
                result += 2 * (i - 1 + 1)
                water = capacity
            
            water -= plants[i]
            result += 1
        
        return result
