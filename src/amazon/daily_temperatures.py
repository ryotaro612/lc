"""

[89,62,70,58,47,47,46,76,100,70]
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        result = [0] * n
        hot = 0
        for i in range(n-1, -1, -1):
            t = temperatures[i]
            if hot <= t:
                hot = t
                continue
                
            days = 1
            while temperatures[i+days] <= t:
                days += result[i+days]
            result[i] = days
        return result                
