"""
125
1
4
"""
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        states = minutesToTest // minutesToDie + 1
        result = 1
        while (states) ** result  < buckets:
            result+= 1
        return result
