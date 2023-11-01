class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        g = self.gcd(max(jug1Capacity, jug2Capacity), min(jug1Capacity, jug2Capacity))
        return targetCapacity % g == 0
    
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
