import heapq

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        heap = []
        for item in s:
            heapq.heappush(heap, item)
        result = 0
        for greed in sorted(g):
            while heap and heap[0] < greed:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                result += 1
        return result
