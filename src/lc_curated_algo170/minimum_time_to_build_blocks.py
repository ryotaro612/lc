import heapq

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        
        heapq.heapify(blocks)

        while len(blocks) > 1:
            heapq.heappop(blocks)
            a = heapq.heappop(blocks)
            heapq.heappush(blocks, a + split)

        return heapq.heappop(blocks)
