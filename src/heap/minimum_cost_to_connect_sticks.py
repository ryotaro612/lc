import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        result = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            result += a + b
            heapq.heappush(sticks, a + b)
            
        return result
