class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        """
        result = 0
        empty = 0
        """
        result = numBottles
        empty = numBottles

        while True:
            if empty < numExchange:
                return result
            empty -= numExchange
            result += 1
            numExchange += 1
            empty += 1
