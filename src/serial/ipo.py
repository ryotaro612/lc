import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        available = []
        not_available = []
        for i in range(len(profits)):
            if capital[i] <= w:
                heapq.heappush(available, -profits[i])
            else:
                heapq.heappush(not_available, [capital[i], profits[i]])
        
        for _ in range(k):
            if available:
                w -= heapq.heappop(available)
            while not_available and not_available[0][0] <= w:
                heapq.heappush(available, -heapq.heappop(not_available)[1])
        return w
