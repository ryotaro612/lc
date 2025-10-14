import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-e for e in piles]
        heapq.heapify(heap)

        for _ in range(k):
            e = heapq.heappop(heap)
            e = abs(e) - abs(e) // 2
            heapq.heappush(heap, -e)

        return -sum(heap)
