import heapq
from collections import Counter
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        """
        result = 0
        heap = [(-5,2), (-2, 4)]
        2222,55 -> 222222
        """
        heap = []
        counter = Counter(nums)
        for num, freq in counter.items():
            heapq.heappush(heap, [-num, freq])
        
        result = 0
        while len(heap) > 1:
            _, freq = heapq.heappop(heap)
            result += freq
            v, next_freq = heapq.heappop(heap)
            heapq.heappush(heap, [v, next_freq + freq])
        return result
