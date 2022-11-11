"""
[11,12,19]
[10,8,7]
19
"""
import heapq

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        n = len(runningCosts)
        result = 0
        end = 0
        heap = []
        total = 0
        for start in range(n):
            end = max(end, start)
            
            while end < n:
                # check total cost
                while heap and heap[0][1] < start:
                    heapq.heappop(heap)
                
                if heap:
                    charge_time = max(-heap[0][0], chargeTimes[end])
                else:
                    charge_time = chargeTimes[end]
                    
                if charge_time + (total + runningCosts[end]) * (end - start + 1) <= budget:
                    total += runningCosts[end]
                    heapq.heappush(heap, (-chargeTimes[end], end))
                    end += 1
                    result = max(result, end - start)
                else:
                    break
            if start < end:
                total -= runningCosts[start]
        
        return result
