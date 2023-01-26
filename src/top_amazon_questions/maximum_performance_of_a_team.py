import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        efsp = sorted([[e, s] for e, s in zip(efficiency, speed)])
        result = 0
        heap = []
        mod = 1000000000 + 7
        sp = 0
        for i in range(n-1, -1, -1):
            result = max(result, efsp[i][0] * (sp + efsp[i][1]))
            heapq.heappush(heap, efsp[i][1])
            sp += efsp[i][1]
            if len(heap) == k:
                sp -= heapq.heappop(heap)
        return result % mod
