import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        """
        """
        heap = [-num for num in nums]
        heapq.heapify(heap)
        result = 0
        for _ in range(k):
            v = -heapq.heappop(heap)
            result += v
            heapq.heappush(heap, -math.ceil(v/3))
        
        return result
