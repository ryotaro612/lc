class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda item: -item[1])
        
        result = 0
        cost = 0
        for num, unit in boxTypes:
            amount = min(num, truckSize - cost)
            result += amount * unit
            cost += amount
        
        return result
