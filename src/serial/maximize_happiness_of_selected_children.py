import heapq

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = [-h for h in happiness]
        heapq.heapify(heap)
        result = 0
        penalty = 0
        while heap and k:
            h = heapq.heappop(heap)
            result += max(0, -h - penalty)
            penalty += 1
            k -= 1
        return result
